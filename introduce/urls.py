from django.urls import path
from . import views

urlpatterns = [
    path('introduce/', views.introduce, name='introduce'),
]