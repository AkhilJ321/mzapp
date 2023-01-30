from django.urls import path
from home import views
urlpatterns = [
    path("", views.home, name='home'),
    path('category', views.category, name='category'),
    path('classifymosquito', views.detect, name='classify'),
    path('scanm', views.detect, name='classify'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('water', views.water, name='water'),
    path('endemic', views.endemic, name='endemic'),
    path('home', views.home, name='main')


]
