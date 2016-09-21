# -*- coding:UTF-8 -*- ＃必须在第一行或者第二行
# -*- coding:gb2312 -*- ＃必须在第一行或者第二行
# -*- coding:GBK -*- ＃必须在第一行或者第二行
from django.forms import ModelForm
from .models import ExamInfo,booklist
from django import forms
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import BootstrapDateInput,BootstrapTextInput,BootstrapUneditableInput
class ExamInfoForm(ModelForm):
    class Meta:
        model = ExamInfo
        fields = '__all__'

class BookList(ModelForm):
    class Meta:
        model = booklist
        fields='__all__'
class LoginForm(forms.Form):
    username = forms.CharField(
            required = True,
            label=u"用户名",
            error_messages={'required':'请输入用户名'},
            widget=forms.TextInput(
                attrs={
                    'placeholder':u"用户名",
                    }
                )
            )

    password = forms.CharField(
            required=True,
            label=u"密码",
            error_messages={'required':u'请输入密码'},
            widget=forms.PasswordInput(
                attrs={
                    'placeholder':u"密码",
                    }
                ),
            )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"用户名和密码为必填项")
        else:
            cleaned_data = super(LoginForm,self).clean()