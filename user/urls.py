from django.urls import path

from . import views

urlpatterns = [
    path('', views.uyeProfil, name='uyeProfil'),
    path('update/', views.updateProfil, name='updateProfil'),
    path('password/', views.changePassword, name='changePassword'),
    path('contents/', views.contents, name='contents'),
    path('comments/', views.comments, name='comments'),
    path('deleteComment/<int:id>/', views.deleteComment, name='deleteComment'),
    path('contentedit/<int:id>/', views.contentedit, name='contentedit'),
    path('deleteContent/<int:id>/', views.deleteContent, name='deleteContent'),
    path('contentaddimage/<int:id>/', views.contentaddimage, name='contentaddimage'),

]
