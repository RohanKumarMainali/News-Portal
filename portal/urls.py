from django.urls import path

from . import views

urlpatterns = [
    path('', views.blogs, name='index'),
    # path('create-package/', views.create_package, name='index'),
    
]