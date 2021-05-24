from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(pre_save, sender=User)
def update_user(sender,instance,**kwargs):
    user = instance
    if user.email != '':
        user.username = user.email
