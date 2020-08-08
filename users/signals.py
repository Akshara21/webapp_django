from django.db.models.signals import post_save
from django_contrib_auth_models import User
from django.dispatch import reciever
from .models import Profile

@reciever(post_save, sender=User)
def create_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@reciever(post_save, sender=User)
def profile_save(sender,instance, **kwargs):
    instance.profile.save()
