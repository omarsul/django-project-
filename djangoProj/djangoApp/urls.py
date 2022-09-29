from django.urls import path     
from . import views

urlpatterns = [
    
    path('', views.index, name="index"),
    path('reg', views.register),
    path('log', views.login),
    path('user/<int:Userid>', views.profile, name="profile" ),
    path('friends', views.friendsTable, name="friends" ),
    path('user/<int:Userid>/del', views.delete, name="del"),
    path('user/<int:Userid>/add', views.add, name="add"),
   
] 