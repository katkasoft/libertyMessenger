from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.main),
    path('logorreg', views.logorreg),
    path('login', views.loginview), 
    path('register', views.registerview),
    path('api/register', views.register)
]
