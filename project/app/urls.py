from django.urls import path
from . import views
urlpatterns = [
path('',views.login),
path('logout',views.logout),
path('home',views.home),
path('display',views.display),
path('edit',views.edit),
path('delete',views.delete),


]