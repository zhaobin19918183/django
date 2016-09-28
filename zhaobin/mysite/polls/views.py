# -*- coding:UTF-8 -*- ＃必须在第一行或者第二行
# -*- coding:gb2312 -*- ＃必须在第一行或者第二行
# -*- coding:GBK -*- ＃必须在第一行或者第二行
# Create your views here.
#-*- encoding:gb2312 -*-
from .models import addForm,booklist,NormalUser,ExamInfo,BlogsPost
import simplejson
from django.core import serializers
from .forms import ExamInfoForm,BookList
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializers import UserSerializer,GroupSerializer,booklistSerializer
from django import forms
from django.template import loader,Context
from django.shortcuts import render_to_response,render
from django.http import HttpResponse ,HttpResponseRedirect
from django.contrib import auth
from django.template.context import RequestContext
from forms import LoginForm
from django.views.generic.list import ListView
from .models import Article, Category
from markdown import markdown
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView
from django.views.generic.dates import YearArchiveView, MonthArchiveView
from django.views.generic import TemplateView
from django.utils.safestring import mark_safe

class JsonTest(simplejson.JSONEncoder ):
    """
    Encoding QuerySet into JSON format.
    """
    def default( self, object ):
        try:
            return serializers.serialize("python", object,
                                          ensure_ascii = False )
        except:
            return simplejson.JSONEncoder.default(self, object )
# 定义转换 json 方法,调用接口返回的是数组
@csrf_exempt
def addForm_json(request):
   json_data = serializers.serialize("json",addForm.objects.all())
   return  HttpResponse(json_data)
# 重名function 不能与 class 重名
def book_json(request):
    print(request)
    json_data = serializers.serialize("json",booklist.objects.all())
    return  HttpResponse(json_data)
def home(request):
    if request.method == 'POST':
        form = ExamInfoForm(request.POST)
        if form.is_valid():
            exam_info = form.save()
            exam_info.save()
            return HttpResponse('Thank you')
    else:
        form = ExamInfoForm()
    return render(request, 'polls/message.html', {'form_info': form})
def testHtml(request):
   return HttpResponse('success')
@csrf_exempt
def book(request):

    if request.method == 'POST':
        form = BookList(request.POST)
        if form.is_valid():
            exam_info = form.save()
            exam_info.save()
            return HttpResponse('Thank you')
    else:
        form = BookList()
    return render(request, 'polls/results.html', {'form_info': form})
# 封装 api
class BookViewSet(viewsets.ModelViewSet):
        """
        允许查看和编辑Book的 API endpoint
        """
        queryset = booklist.objects.all()
        serializer_class = booklistSerializer
class UserViewSet(viewsets.ModelViewSet):
        """
        允许查看和编辑user 的 API endpoint
        """
        queryset = User.objects.all()
        serializer_class = UserSerializer
class GroupViewSet(viewsets.ModelViewSet):
        """
        允许查看和编辑group的 API endpoint
        """
        queryset = Group.objects.all()
        serializer_class = GroupSerializer
        #
#html
class NormalUserForm(forms.Form):
  username = forms.CharField()
  headImg  = forms.FileField()
def registerNormalUser(request):

  if request.method == "POST":
    uf = NormalUserForm(request.POST,request.FILES)
    if uf.is_valid():
      # get the info of the form  cleaned_data :处理或得到的数据,让 username 和 uf 获得数据类型一致
      username = uf.cleaned_data['username']
      headImg  = uf.cleaned_data['headImg']
      # write in database
      normalUser = NormalUser()
      normalUser.username = username
      normalUser.headImg  = headImg
      normalUser.save()
      return HttpResponse('Upload Succeed!')
  else:
    uf = NormalUserForm()
  return render(request,'polls/register.html',{'uf':uf})
#文件存储 ios
@csrf_exempt
def fileUpload(request):
  if request.method   == 'POST':
    name              = request.POST.get('name')
    #files 是上传的文件流通过对应的参数名获取
    image             = request.FILES.get('image')
    filesUpload       = ExamInfo()
    filesUpload.level = image
    filesUpload.name  = name
    filesUpload.save()
    return HttpResponse('success')
#注册
class UserForm(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    passworld = forms.CharField(label='密码：',max_length=52)
    email = forms.EmailField(label='电子邮件：')
# Create your views here.
def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            passworld = uf.cleaned_data['passworld']
            email = uf.cleaned_data['email']
            #将表单写入数据库
            user = User.objects.create_superuser(username,email,passworld)
            if user.is_staff:
             print ("注册失败")
            else:
             user.save()
            return HttpResponse('success')
    else:
        uf = UserForm()
    return render(request,'polls/register.html',{'uf':uf})
# Create your views here.
def archive(request):
    posts = BlogsPost.objects.all()
    t = loader.get_template("polls/archive.html")
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))
#login
def login(request):

    if request.method == 'GET':
       form = LoginForm()

       if request.user.is_authenticated():
        content = BlogsPost.objects.all()
        username =request.session['username']
        print("用户已登陆")
        return render_to_response('polls/index.html',{'username':username,'content':content},RequestContext(request))

       else:
           print("用户未登陆")
       return render_to_response('polls/login.html',RequestContext(request,{'form':form,}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            user = auth.authenticate(username=username,password=password)
            if user is not None and user.is_active:
                auth.login(request,user)
                #将用户名传递给前台页面显示
                request.session['username'] =username
                #将所需要的数据传递出去
                content = BlogsPost.objects.all()

                return render_to_response('polls/index.html',{'username':username,'content':content},RequestContext(request))
            else:
                return render_to_response('polls/login.html',RequestContext(request,{'form':form,'password_is_wrong':True}))
        else:
            return render_to_response('polls/login.html',RequestContext(request,{'form':form,}))
#loginOut
@csrf_exempt
def logout(request):
    print(request)
    if request.method == 'GET':
      auth.logout(request)
      form = LoginForm()
      return render_to_response('polls/login.html',RequestContext(request,{'form':form,}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            user = auth.authenticate(username=username,password=password)
            if user is not None and user.is_active:
                auth.login(request,user)
                #将用户名传递给前台页面显示
                request.session['username'] =username
                #将所需要的数据传递出去
                content = BlogsPost.objects.all()
                return render_to_response('polls/index.html',{'username':username,'content':content},RequestContext(request))
            else:
                return render_to_response('polls/login.html',RequestContext(request,{'form':form,'password_is_wrong':True}))
        else:
            return render_to_response('polls/login.html',RequestContext(request,{'form':form,}))
#博客demo

class IndexView(ListView):
    template_name = "blog/index.html"

    def get_queryset(self):
        return Article.objects.filter(status='p')


class BlogView(ListView):
    template_name = "blog/blog.html"

    def get_queryset(self):
        return Article.objects.filter(status='p')


class AboutView(TemplateView):
    template_name = 'blog/about.html'


class ContactView(TemplateView):
    template_name = 'blog/contact.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/detail.html"
    pk_url_kwarg = 'article_id'

    def get_object(self, queryset=None):
        obj = super(ArticleDetailView, self).get_object(queryset=None)
        obj.body = mark_safe(markdown.markdown(obj.body, extras=['fenced-code-blocks', 'code-friendly', 'codehilite']))
        # BUG:必须在这里渲染，如果在模板中通过模板标签渲染则格式会乱掉
        obj.viewed()
        return obj


class CategoryView(ListView):
    template_name = "blog/index.html"

    def get_queryset(self):
        return Article.objects.filter(category=self.kwargs['category_id'], status='p')


class TagView(ListView):
    template_name = "blog/index.html"

    def get_queryset(self):
        return Article.objects.filter(tags=self.kwargs['tag_id'], status='p')


class ArticleYearArchiveView(YearArchiveView):
    queryset = Article.objects.all()
    date_field = "created_time"
    make_object_list = True
    context_object_name = 'article_list'
    template_name = 'blog/index.html'


class ArticleMonthArchiveView(MonthArchiveView):
    queryset = Article.objects.all()
    date_field = "created_time"
    context_object_name = 'article_list'
    template_name = 'blog/index.html'
    month_format = '%m'


