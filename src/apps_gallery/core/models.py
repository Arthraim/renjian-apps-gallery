# coding=UTF8
from django.db import models

        
class Developer(models.Model):
    screen_name = models.CharField(max_length=30, primary_key=True)
    nickname = models.CharField(max_length=30)
    email = models.EmailField(max_length=75)
    homepage = models.URLField(max_length=100, blank=True)
    bio = models.CharField(max_length=200, blank=True)
    
    def __unicode__(self):
        return self.screen_name
    
    class Meta:
        ordering = ('screen_name',)

class Tag(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
        
        
class App(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    intro = models.CharField(max_length=100)
    version = models.CharField(max_length=30)
    
    homepage = models.URLField(max_length=100, blank=True)
    dowload_url = models.URLField(max_length=100, blank=True)
    opensource = models.URLField(max_length=100, blank=True)
    thumbnail_url = models.URLField(max_length=100, blank=True)
    
    developers = models.ManyToManyField(Developer)
    tags = models.ManyToManyField(Tag)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)




