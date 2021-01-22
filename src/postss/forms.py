from django import forms
from .models import Comment, Work
class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'gender', 'number','cv')

class WorkCreateForm(forms.ModelForm):
    title = forms.CharField(label='عنوان العمل')
    content = forms.CharField(label=' تفاصيل العمل', widget=forms.Textarea)
    class Meta:
        model = Work
        fields = ['title', 'content'] 