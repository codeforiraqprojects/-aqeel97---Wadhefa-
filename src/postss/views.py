from django.shortcuts import render, get_object_or_404, redirect
from .models import Work, Comment
from .forms import NewComment, WorkCreateForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

from django.core.files.storage import FileSystemStorage #to file


def home(request):
    works = Work.objects.all()
    paginator = Paginator(works, 5)
    page = request.GET.get('page')
    try:
        works = paginator.page(page)
    except PageNotAnInteger:
        works = paginator.page(1)
    except EmptyPage:
        works = paginator.page(paginator.num_page)
    context = {
        'title' : 'الصفحه الرئيسيه',
        'works' : works,
        'page' : page,
    }
    return render(request, 'postss/index.html',context)

def about(request):
    return render(request, 'postss/about.html',{'title' : 'من انا'})


def work_detail(request, work_id):
    work = get_object_or_404(Work, pk=work_id)
    comments = work.comments.filter() #comments = related_name in models.py
    if request.method == 'POST':
        comment_form = NewComment(request.POST, request.FILES)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.work = work
            new_comment.save()
            comment_form = NewComment()
            messages.success(request, f' {new_comment.name} لقد تم التقديم بنجاح')
            return redirect('home')

    else:
        comment_form = NewComment()
    context = {
        'title' : work,
        'work' : work,
        'comments' : comments,        
        'comment_form' : comment_form,
    }
    
    return render(request, 'postss/detail.html', context)

class WorkCreateView(LoginRequiredMixin, CreateView):
    model = Work
    template_name = 'postss/new_work.html'
    form_class = WorkCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class WorkUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Work
    template_name = 'postss/work_update.html'
    form_class = WorkCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):# to chack 
        work = self.get_object()
        if self.request.user == work.author:
            return True
        else:
            return False

class WorkDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Work
    success_url ='/'
    def test_func(self):# to chack 
        work = self.get_object()
        if self.request.user == work.author:
            return True
        return False