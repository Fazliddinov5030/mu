from django.urls import path
from . import views

app_name = 'project2'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('post/', views.home_page, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
]
