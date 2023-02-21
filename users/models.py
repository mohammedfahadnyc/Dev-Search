from django.db import models

# Create your models here.
from django.contrib.auth.models import User
import uuid
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(null=True,blank=True,max_length=255)
    email = models.EmailField(blank=True,null=True)
    short_intro = models.CharField(max_length=200,null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    username = models.CharField(max_length=255,null=True,blank=True)
    profile_image = models.ImageField(null=True,blank=True,upload_to='profiles/',default="images/profile-pics/user-default.png")
    social_github = models.CharField(max_length=200,null=True,blank=True)
    social_linkedin = models.CharField(max_length=200, null=True, blank=True)
    social_stack_over_flow = models.CharField(max_length=200, null=True, blank=True)
    social_youtube = models.CharField(max_length=200, null=True, blank=True)
    social_twitter = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    location = models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        if not self.name and self.username :
            return str(self.username)
        return str(self.name)


class Skill(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(max_length=500,blank=True,null=True)
    owner = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.name)







