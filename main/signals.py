from django.db.models.signals import post_save #Import a post_save signal when a user is created
 # Import the built-in User model, which is a sender
from django.dispatch import receiver # Import the receiver
from .models import AudienceAdditional, Audience


@receiver(post_save, sender=Audience)
def create_profile(sender, instance, created, **kwargs):
    if created:
        AudienceAdditional.objects.create(user=instance)


@receiver(post_save, sender=Audience)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()