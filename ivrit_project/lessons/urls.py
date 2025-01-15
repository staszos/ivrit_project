from django.urls import path
from .views import layout, lessons
from . import views




urlpatterns = [
    path('', views.layout, name='layout'),
    path('lesson1', views.lessons, name='lesson1'),
    path('target_view/', views.lessons),
    
]