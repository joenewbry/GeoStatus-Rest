from django.db import models
from django.contrib.gis.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Location(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    owner = models.ForeignKey('auth.User', related_name='locations')

class Context(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    context = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    mpoly = models.MultiPolygonField(srid=4326)
    owner = models.ForeignKey('auth.User', related_name='contexts')

class Status(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='status')

class Meta:
    Ordering = ('created',)
    def __str__(self):
        return self.name

# Signal hooks
@receiver(post_save, sender=Location)
def create_new_status(sender, **kwargs):
    if kwargs.get('created', True):
        location = kwargs.get('instance')
        longitude = location.longitude
        latitude = location.latitude
        point = "POINT({} {})".format(longitude, latitude)
        user_contexts = Context.objects.filter(owner=location.owner)
        contexts = user_contexts.filter(mpoly__contains=point)
        if len(contexts) > 0:
            context = contexts[0]
            status = Status(name=context.context, owner=context.owner)
            status.save()
        else:
            status = Status(name="Unknown", owner=context.owner)
            status.save()
