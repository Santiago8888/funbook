from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    owner = models.ForeignKey(User, related_name='question_user', verbose_name='Owner')
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True,blank = True)
    question_body = models.TextField(max_length=1000, blank = True)
    def __unicode__(self):
	return self.question_text


class Comment(models.Model):
    question = models.ForeignKey(Question, related_name='comments')
    ownerComment = models.ForeignKey(User, related_name='comment_user', verbose_name='OwnerComment',blank=True)
    comment_text = models.TextField(max_length=600)
    comment_date = models.DateTimeField(auto_now_add=True, blank=True)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.comment_text
