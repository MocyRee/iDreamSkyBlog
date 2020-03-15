from django.db import models
from django.utils import timezone
from blog.models import Article


class Comment(models.Model):
    body = models.TextField('正文', max_length=300)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_mod_time = models.DateTimeField('修改时间', auto_now=True)
    author = models.CharField(max_length=50)
    article = models.ForeignKey(Article, verbose_name='文章', on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', verbose_name="上级评论", blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        verbose_name = "评论"
        verbose_name_plural = verbose_name
        get_latest_by = 'id'

    def __str__(self):
        return self.body