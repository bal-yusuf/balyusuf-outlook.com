

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addComment/<int:id>/', views.addComment, name='addComment'),
    path('addContent/', views.addContent, name='addContent'),





]