from django.db import models
from django.utils.timezone import now


class Message(models.Model):

    content = models.TextField('留言内容')
    author = models.CharField('作者', max_length=50)
    contact = models.CharField('邮箱', max_length=254, blank=True)
    website = models.URLField('网址', max_length=200, blank=True)
    created_time = models.DateTimeField('留言时间', auto_now=True)

    class Meta:
        verbose_name = '私信'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.author    