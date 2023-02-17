import uuid

from django.db import models
from users.models import Profile
# Create your models here.
class Project(models.Model):
    owner = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    featured_image = models.ImageField(blank=True,null=True,default='default.jpg')
    description = models.TextField(null=True,blank=True)
    demo_link = models.CharField(max_length=2000,null=True,blank=True)
    source_link = models.CharField(max_length=2000,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    tags = models.ManyToManyField('Tag',blank=True) #many-many with Class Tag

    #handling up or downvotes
    vote_total = models.IntegerField(default=0,null=True,blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title

class Review (models.Model):
    body = models.TextField(null=True,blank=True)
    VOTE_TYPE = (('Up','UP Vote'), ('Down','Down'))
    value = models.CharField(max_length=200,choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False,primary_key=True,unique=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)  #many-one with Project Class

    def __str__(self):
        return self.value


class Tag(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    name =  models.CharField(max_length=200)

    def __str__(self):
        return self.name

