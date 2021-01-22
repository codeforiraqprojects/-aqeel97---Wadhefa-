from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Work(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    work_date = models.DateTimeField(default=timezone.now)
    work_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
       return reverse('detail', args=[self.pk])
    class Meta:
        ordering = ('-work_date',)


class Comment(models.Model):
    name = models.CharField(max_length=50, verbose_name='الاسم الكامل')
    email = models.EmailField(verbose_name=' البريد الالكتروني')
    number = models.BigIntegerField(verbose_name='رقم الهاتف')
    gender = models.CharField(max_length=50, verbose_name='الجنس')
    cv = models.FileField(upload_to='cv_pdf', verbose_name='السيره الذاتيه')
    work = models.ForeignKey(Work, on_delete= models.CASCADE, related_name='comments')
    def __str__(self):
        return self.name

