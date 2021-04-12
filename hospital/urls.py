from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('', views.contact, name="contact"),
    path('', views.pricing, name="pricing"),
    path('service/', views.service, name="service"),
    path('', views.blog, name="blog"),
    path('signup/', views.signup, name='signup'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('admin_homepage/', views.admin_homepage, name='admin_homepage'),
    path('patient_homepage/', views.patient_homepage, name='patient_homepage'),
    path('doctor_homepage/', views.doctor_homepage, name='doctor_homepage'),
    path('receptionist_homepage/', views.receptionist_homepage, name='receptionist_homepage'),
    ]
