from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label=' اسم المستخدم', max_length=30, help_text='اسم المستخدم يجب ان لا يحتوي على مسافات')
    email = forms.EmailField(label= 'البريد الالكتروني')
    first_name = forms.CharField(label='الاسم الاول', max_length=20)
    last_name = forms.CharField(label='الاسم الثاني', max_length=20)
    password1 = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput(), min_length=8, help_text='كلمة المرور يجب ان لا تقل عن 8 ')
    password2 = forms.CharField(label='اعادة كلمة المرور', widget=forms.PasswordInput(), min_length=8)
    active = forms.BooleanField(label='__صاحب عمل')
    class Meta:
        model = User
        fields  = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
    def clean_password(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password1']:
            raise forms.ValidationError('كلمة المرور غير متطابقه')
        return cd['password2']
    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('يوجد مستخدم بهذا الاسم')
        return cd['username']
class LoginForm(forms.ModelForm):
    username = forms.CharField(label='البريد الالكتروني')
    password = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password')

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='الاسم الاول')
    last_name = forms.CharField(label='الاسم الثاني')
    email = forms.EmailField(label= 'البريد الالكتروني')
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)