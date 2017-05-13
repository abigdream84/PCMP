from django.db import models

# Create your models here.


class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True,null=True)
    memo = models.TextField(blank=True,null=True)
    create_at = models.DateTimeField(blank=True,auto_now_add=True)
    update_at = models.DateTimeField(blank=True,auto_now=True)
    


class AdminInfo(models.Model):
    user = models.OneToOneField('UserProfile')
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Status(models.Model):
    name = models.CharField(max_length=64)
    memo = models.TextField(blank=True,unique=True)
    

class Host(models.Model):
    hostname = models.CharField(max_length=128,unique=True)
    ipaddrs = models.GenericIPAddressField(blank=True,null=True)
    cpu = models.IntegerField(blank=True,null=True)
    memory = models.IntegerField(blank=True,null=True)
    disk = models.CharField(max_length=64,blank=True,null=True)
    status = models.ForeignKey('Status')
    create_at = models.DateTimeField(blank=True,auto_now_add=True)
    update_at = models.DateTimeField(blank=True,auto_now=True)
    userpro = models.ForeignKey('UserProfile',null=True,blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=32,unique=True)
    host_tag = models.ManyToManyField('Host')
    creater = models.ForeignKey('UserProfile',blank=True,null=True)


    

    




