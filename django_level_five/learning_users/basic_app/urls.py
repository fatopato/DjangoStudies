from django.urls import path
from . import views


app_name = 'basic_app'

urlpatterns=[
    path('register', views.register_view, name='register'),
    path('user_login', views.user_login_view, name='user_login'),
]
