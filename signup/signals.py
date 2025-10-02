from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from profile_user.models import profile_user_model


@receiver(post_save, sender=User)
def create_user_profile(sender , instance, created, **kwargs):
    if created:
        profile_user_model.objects.create(user=instance)
        print("profile user create".upper())
