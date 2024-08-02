
from django.urls import path
from . import views

urlpatterns = [
    path('', views.authView,name="authview"),
    path('login/',views.authView1,name="authview1"),
]
