from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ManyToManyField, OneToOneField,\
    ForeignKey

# Create your models here.


class user(models.Model):
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    user_type = models.ForeignKey('usertype')

class usertype(models.Model):
    name = models.CharField(max_length=100,unique=True)

class group(models.Model):
    groupname = models.CharField(max_length=50, unique=True)
    user = models.ManyToManyField('user')

class userinfo(models.Model):
    department = models.CharField(max_length=50,default='')
    user_relation = OneToOneField('user')
        
class host(models.Model):
    hostname = models.CharField(max_length=256)
    ip = models.GenericIPAddressField()
    user_group = models.ForeignKey('group')

    



