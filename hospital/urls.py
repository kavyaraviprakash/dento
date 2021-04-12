from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import userprofile, AppointmentListView, EmpListView, AppointmentDeleteView, empAppEdit

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name='contact'),
    path('', views.pricing, name="pricing"),
    path('service/', views.service, name="service"),
    path('', views.blog, name="blog"),
    path('signup/', views.signup, name='signup'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('employee_homepage/', views.employee_homepage, name='employee_homepage'),
    path('patient_homepage/', views.patient_homepage, name='patient_homepage'),
    path('doctor_homepage/', views.doctor_homepage, name='doctor_homepage'),
    path('receptionist_homepage/', views.receptionist_homepage, name='receptionist_homepage'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('patient_edit/', userprofile.as_view(), name='userprofile'),
    path('appoinmentlist/', AppointmentListView.as_view(), name='AppointmentListView'),
    path('employeelist/', EmpListView.as_view(), name='EmpListView'),
    path('<int:pk>/delete/', AppointmentDeleteView.as_view(), name='AppointmentDeleteView'),
    path('<int:pk>/update/', empAppEdit.as_view(), name='empAppEdit'),
    path('appointment/', views.MakeAppointments, name='MakeAppointments'),
    path('addappointment/', views.AddAppointment, name='AddAppointment'),
    #path('empappointment/', views.emp_appointment, name='emp_appointments'),
    path('reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name = 'password_reset_complete.html'), name='password_reset_complete'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name ='password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name = 'password_change_done.html'), name='password_change_done'),
    ]
