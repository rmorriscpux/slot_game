from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('game/', views.game_page),
    path('game/spin/', views.game_spin),
    path('user/', views.user_info),
    path('user/history/', views.show_history),
    path('user/add_credit/', views.add_credit),
]

if settings.DEBUG:
    urlpatterns.append(path('test/', views.test_page))