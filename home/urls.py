from django.urls import path
from home import views
urlpatterns = [
   path("",views.home,name='home'),
   path('home',views.home,name = 'home'),
   path('classifymosquito',views.detect,name = 'classify'),
   path('scanm',views.detect,name = 'classify'),
   path('about',views.about,name='about'),
   path('contact',views.contact,name='contact'),
   path('water',views.water,name='water'),


]
