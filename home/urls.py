from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('send-mail/', views.sendMail, name="send-mail"),
]
