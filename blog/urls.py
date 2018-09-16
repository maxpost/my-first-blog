from django.urls import path
from . import views

urlpatterns = [
    path('post', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('xxxx',views.home,name='home'),
    path('resume',views.resume,name='resume'),
    path('apps',views.apps,name='apps'),
]
