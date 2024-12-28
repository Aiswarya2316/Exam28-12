from django.urls import path
from . import views
urlpatterns = [
path('',views.login),
path('register',views.register),
path('logout',views.logout),
path('home',views.home),
path('add',views.add),
path('display',views.display, name='display'),
path('edit/<int:id>/', views.edit, name='edit'),
path('delete/<int:id>/', views.delete, name='delete'),


]