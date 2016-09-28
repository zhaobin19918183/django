# -*- coding:UTF-8 -*- ＃必须在第一行或者第二行
# -*- coding:gb2312 -*- ＃必须在第一行或者第二行
# -*- coding:GBK -*- ＃必须在第一行或者第二行
from __future__ import unicode_literals
import sys
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib import admin
reload(sys)
sys.setdefaultencoding("utf-8")
from django.db import models
class Item(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('item_detail', None, {'object_id': self.id})
# Create your models here.
#IOS 上传文件部分
# Photologue image path relative to media root
class ExamInfo(models.Model):
    #unique=True　检测是否重复(不允许重复)
    name = models.CharField(max_length=10,verbose_name="用户名",unique=True)
    level = models.ImageField(verbose_name="头像",blank=True)
    #列表显示图片方法

    def admin_sample(self):
        return '<img src="/templates/%s" height="50" width="50" />' %(self.level)
    admin_sample.short_description = '缩略图'
    admin_sample.allow_tags = True

    #改变 form 的名称
    class Meta:
        verbose_name = "IOS"
        verbose_name_plural = "IOS"
    def __str__(self):
        return self.name
class addForm(models.Model):
    num = models.CharField(max_length=30, verbose_name="序号")
    kid = models.CharField(max_length=60, verbose_name="文件分类")
    name = models.CharField(max_length=50, verbose_name="文件名称")
    gjz = models.CharField(max_length=50, verbose_name="关键字", blank=True)
    fj = models.CharField(max_length=30, verbose_name="附件", blank=True)
    status = models.CharField(max_length=60, verbose_name="状态")
    where = models.CharField(max_length=30, verbose_name="存放位置")
    headImg = models.FileField(upload_to='./upload', verbose_name="上传")
    bz = models.CharField(max_length=50, verbose_name="备注", blank=True)

    class Meta:
        verbose_name = "文件目录"
        verbose_name_plural = "文件目录"

    def __str__(self):
        return self.name
class booklist(models.Model):
    name = models.CharField(max_length=20,verbose_name="编号")
    date = models.DateField(verbose_name="出版时间")
    number = models.CharField(max_length=10,verbose_name="书籍名称")
    class Meta:
         verbose_name = "图书列表"
         verbose_name_plural = "图书列表"
    def __str__(self):
          return self.name
class NormalUser(models.Model):
  username = models.CharField(max_length=30)
  headImg = models.FileField(upload_to='./upload')
  def __unicode__(self):
    return self.username
  class Meta:
    ordering = ['username']
  def admin_sample(self):
        return '<img src="/templates/%s" height="50" width="50" />' %(self.level)
  admin_sample.short_description = '缩略图'
  admin_sample.allow_tags = True
class MyUser(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=20, null=True, blank=True)
    avatar = models.ImageField(upload_to='photo', null=True, blank=True)
class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    class Meta:
     ordering = ('-timestamp',)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')
admin.site.register(BlogsPost,BlogPostAdmin)
#博客 demo
class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )

    title = models.CharField('标题', max_length=70)
    body = models.TextField('正文')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES)
    abstract = models.CharField('摘要', max_length=54, blank=True, null=True,
                                help_text="可选，如若为空将摘取正文的前54个字符")
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    topped = models.BooleanField('置顶', default=False)

    category = models.ForeignKey('Category', verbose_name='分类',
                                 null=True,
                                 on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-pub_time']
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ['-last_modified_time']


class Category(models.Model):
    name = models.CharField('类名', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'article_id': self.pk})

    def save(self, *args, **kwargs):
        self.summary = self.summary or self.body[:120]
        self.save(*args, **kwargs)

    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])
    class Meta:
        ordering = ['name']
        verbose_name = "分类"
        verbose_name_plural = verbose_name
class Tag(models.Model):
    name = models.CharField('标签名', max_length=30)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_mod_time = models.DateTimeField('修改时间', auto_now=True)

    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['name']
        verbose_name = "标签"
        verbose_name_plural = verbose_name
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Category)