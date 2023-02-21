from django.db.models.signals import post_save,post_delete
from users.models import Profile
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(post_save,sender=User)
def createProfile(sender,instance,created,**kwargs):
    if created :
        user = instance
        profile = Profile.objects.create(user=user,username=user.username,email=user.email,name=user.first_name)
# post_save.connect(createProfile,sender=User)



@receiver(post_delete,sender=Profile)
def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass
# post_delete.connect(deleteUser, sender=Profile)