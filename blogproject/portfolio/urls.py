from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('writepf/', views.writepf, name='writepf'),
    path('createpf/', views.createpf, name='createpf'),
]