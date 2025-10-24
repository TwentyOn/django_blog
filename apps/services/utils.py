from pytils.translit import slugify
from uuid import uuid4


def unique_slug(instance, string, slug_field):
    model = instance.__class__
    if not slug_field:
        slug_field = slugify(string)
    if model.objects.filter(slug=slug_field).exclude(pk=instance.pk).exists():
        slug_field = f'{slug_field}-{uuid4().hex[:8]}'
    return slug_field