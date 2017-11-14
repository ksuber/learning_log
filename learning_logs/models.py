from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Topic(models.Model):
    ''' A topic the user is learning about '''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        '''Returns text as a string'''
        return self.text


class Entry(models.Model):
    ''' Something learned about a topic'''
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        '''Returns string of object'''
        return self.text[:50] + '....'
