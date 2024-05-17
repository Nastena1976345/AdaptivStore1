from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('test_index/', views.test_index, name='test_index'),
]
