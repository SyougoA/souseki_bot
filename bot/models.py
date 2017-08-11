from django.db import models

# Create your models here.
class Comment(models.Model):
    reply_user = models.CharField(max_length=32)
    comment_text = models.CharField('comment_contents', max_length=100)
