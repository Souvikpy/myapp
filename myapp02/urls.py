from django.urls import path
from myapp02 import views

app_name = "myapp02"

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('child/', views.child, name='child'),
]
