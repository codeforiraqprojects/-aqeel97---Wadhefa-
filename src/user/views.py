from django.shortcuts import render,redirect
from .forms import UserCreationForm, LoginForm, UserUpdateForm, ProfilUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from postss.models import Work
from django.contrib.auth.decorators import login_required   
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            #username = form.cleaned_data['username']
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            messages.success(request, f'تهانينا {new_user} لقد تمت عملية التسجيل بنجاح')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {
        'title' : 'التسجيل',
        'form' : form,
    })

def login_user(request):
    if request.method == 'POST':
        form = LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.warning(request, 'هناك خطا في البريد الالكتروني او كلمة المرور ')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {
        'title' : 'تسجيل الدخول',
        'form' : form,
    })
def logout_user(request):
    logout(request)
    return render(request, 'user/logout.html',{
        'title' : 'تسجيل الخروج',
    })
@login_required(login_url='login')
def profile(request):
    works = Work.objects.filter(author=request.user)
    return render(request, 'user/profile.html', {
        'title' : 'الملف الشخصي',
        'works' : works
    })
@login_required(login_url='login')
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfilUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            messages.success(request, 'ام تحديث الملف الشخصي')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfilUpdateForm(instance=request.user.profile)

    context = {
        'title' : 'تعديل الملف الشخصي',
        'user_form' : user_form,
        'profile_form' : profile_form,
    }
    return render(request,'user/profile_update.html', context)
