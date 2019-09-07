from django.contrib import admin
from django.conf.urls import url
from django.urls import include
from . import views

urlpatterns = [
    #url('',views.game_login,name='game_login'),
    url('',views.hello_world,name='hello_world'),
]