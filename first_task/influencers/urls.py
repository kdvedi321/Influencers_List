from django.urls import path
from django.urls import include
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_data/', views.get_data, name='get_data'),
]
