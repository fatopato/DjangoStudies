from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fatih', views.fatih, name='fatih'),
    path('access', views.access, name='access'),

]
