from django.db.models.signals import pre_save
from .models import HowWeWork
from .utils import unique_slug_generator


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=HowWeWork)
