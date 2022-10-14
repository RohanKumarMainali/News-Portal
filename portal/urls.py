from django.urls import path

from . import views

urlpatterns = [
    path('', views.package_list, name='index'),
    # path('create-package/', views.create_package, name='index'),
    
]