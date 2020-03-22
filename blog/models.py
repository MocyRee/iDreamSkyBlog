from django.db import models
from django.urls import reverse
from django.utils.timezone import now
import markdown


class Log(models.Model):

    pub_time = models.DateTimeField(blank=False, null=False, default=now)
    body = models.TextField()

    class Meta:
        ordering = ['-pub_time']

class Article(models.Model):
    ALLOW_COMMENT = (
        ('0', 'yes'),
        ('1', 'no')
    )


    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField('Created time', default=now)
    modified_time = models.DateTimeField('Modified time', default=now)
    pub_time = models.DateField(blank=False, null=False, default=now)
    allow_comment = models.CharField("评论开关", max_length=1, choices=ALLOW_COMMENT)
    views = models.PositiveIntegerField('浏览', default=0)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField("Tag", blank=True)
    order = models.IntegerField('优先级', default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name = 'article'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.id})

    # def save(self, *args, **kwargs):
    #     md = markdown.Markdown(extensions=[
    #         'markdown.extensions.extra',
    #         'markdown.extensions.codehilite',
    #     ])
    #     self.body = md.convert(self.body)
    #     super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(default='no-slug', max_length=30, blank=True)
    display = models.BooleanField(default=False)
    img = models.URLField(max_length=200, blank=True)
    size = models.SmallIntegerField(default=6)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse('blog:category_detail', kwargs={'category_name':self.slug})

class Tag(models.Model):
    name = models.CharField("标签", max_length=20)
    slug = models.SlugField(max_length=30, blank=True)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Nav(models.Model):

    name = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    style = models.TextField(blank=True)
    sequence = models.IntegerField('排序', unique=True)
    is_enable = models.BooleanField('是否启用', default=True)

    class Meta:
        ordering = ['sequence']
        verbose_name = '导航栏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.content[0:4] == 'http':
            return self.content
        else:
            url = self.content
            return reverse(url)
            
    


class NavCollapse(models.Model):

    name = models.CharField('标题', max_length=50)
    content = models.TextField()
    sequence = models.IntegerField('排序', unique=True)
    is_enable = models.BooleanField('是否启用', default=True)
    parent = models.ForeignKey(Nav, on_delete=models.CASCADE)

    class Meta:
        ordering = ['sequence']
        verbose_name = '导航子菜单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Links(models.Model):

    name = models.CharField('链接名称', max_length=30, unique=True)
    link = models.URLField('链接地址')
    sequence = models.IntegerField('排序', unique=True)
    is_enable = models.BooleanField('是否显示', default=True, blank=False, null=False)
    show_type = models.CharField('显示类型', max_length=1)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_mod_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        ordering = ['sequence']
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BlogSettings(models.Model):

    sitename = models.CharField("网站名称", max_length=200, null=False, blank=False, default='')
    site_description = models.TextField("网站描述", max_length=1000, null=False, blank=False, default='')
    site_seo_description = models.TextField("网站SEO描述", max_length=1000, null=False, blank=False, default='')
    site_keywords = models.TextField("网站关键字", max_length=1000, null=False, blank=False, default='')
    article_sub_length = models.IntegerField("文章摘要长度", default=300)
    sidebar_article_count = models.IntegerField("侧边栏文章数目", default=10)
    sidebar_comment_count = models.IntegerField("侧边栏评论数目", default=5)
    show_google_adsense = models.BooleanField('是否显示谷歌广告', default=False)
    google_adsense_codes = models.TextField('广告内容', max_length=2000, null=True, blank=True, default='')
    open_site_comment = models.BooleanField('是否打开网站评论功能', default=True)
    beiancode = models.CharField('备案号', max_length=2000, null=True, blank=True, default='')
    analyticscode = models.TextField("网站统计代码", max_length=1000, null=False, blank=False, default='')
    show_gongan_code = models.BooleanField('是否显示公安备案号', default=False, null=False)
    gongan_beiancode = models.TextField('公安备案号', max_length=2000, null=True, blank=True, default='')
    resource_path = models.CharField("静态文件保存地址", max_length=300, null=False, default='/var/www/resource/')

    class Meta:
        verbose_name = '网站配置'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sitename

    def clean(self):
        if BlogSettings.objects.exclude(id=self.id).count():
            raise ValidationError(_('只能有一个配置'))

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

