from django import template
from postss.models import Work

register = template.Library()
@register.inclusion_tag('postss/latest_work.html')
def latest_work():
    context = {
        'l_work' : Work.objects.all()[0:5]
    }
    return context