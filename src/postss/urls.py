from django.urls import path
from . import views
from .views import WorkCreateView, WorkUpdateView, WorkDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('',views.home, name = 'home'),
    path('about/',views.about, name = 'about'),
    path('detail/<int:work_id>/', views.work_detail, name = 'detail'),
    path('new_work/', WorkCreateView.as_view(), name='new_work'),
    path('detail/<slug:pk>/update/', WorkUpdateView.as_view(), name='work-update'),
    path('detail/<slug:pk>/delete/', WorkDeleteView.as_view(), name='work-delete'),
]
