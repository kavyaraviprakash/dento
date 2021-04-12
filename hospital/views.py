from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DeleteView, UpdateView

from .models import Patient, Appointment

from hospital.forms import CustomUserCreationForm, CustomUserChangeForm, AppointmentForm


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def pricing(request):
    return render(request, 'templates/pricing.html', {})


def service(request):
    return render(request, 'service.html')


def blog(request):
    return render(request, 'templates/blog.html', {})


def home(request):
    if request.user.is_authenticated:
        userT = request.user
        if userT.is_superuser:
            print("SENDING A SUPERUSER")
            return redirect('employee_homepage')
            # return HttpResponseRedirect(reverse('admin:index'))
        elif str(userT.groups.get()) == 'patient':
            return redirect('patient_homepage')
        elif str(userT.groups.get()) == 'doctor':
            return redirect('doctor_homepage')
        elif str(userT.groups.get()) == 'receptionist':
            return redirect('receptionist_homepage')
    else:
        return render(request, 'base.html')


def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        print(user)

        if user is not None:
            if user.is_active:
                print("GROUPS" + str(user.groups))
                login(request, user)
            if user.is_superuser:
                print("SENDING A SUPERUSER")
                return redirect('employee_homepage')
                # return HttpResponseRedirect(reverse('admin:index'))
            elif str(user.groups.get()) == 'patient':
                return redirect('patient_homepage')
            elif str(user.groups.get()) == 'receptionist':
                return redirect('receptionist_homepage')
            elif str(user.groups.get()) == 'doctor':
                return redirect('doctor_homepage')
        else:
            info = 'Username OR password is incorrect'
            form = AuthenticationForm(request.POST)
            return render(request, 'registration/login.html', {'form': form, 'info': info})
    else:
        form = AuthenticationForm(request.POST)
        return render(request, 'registration/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            group = Group.objects.get(name='patient')
            user.groups.add(group)
            user.is_patient = True
            user.save()
            return redirect('patient_homepage')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def employee_homepage(request):
    return render(request, 'employee_homepage.html')


def patient_homepage(request):
    return render(request, 'patient_homepage.html')


def receptionist_homepage(request):
    return render(request, 'receptionist_homepage.html')


def doctor_homepage(request):
    return render(request, 'doctor_homepage.html')


def logoutuser(request):
    logout(request)
    return redirect('home')


class userprofile(generic.UpdateView):
    form_class = CustomUserChangeForm
    template_name = 'pateintprofile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


def MakeAppointments(request):
    submitted = False
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return HttpResponseRedirect('/appointment?submitted=True')
    else:
        form = AppointmentForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'makeappointments.html', {'form': form, 'submitted': submitted})


class AppointmentListView(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'patientviewappointments.html'

    def get_queryset(self):
        if self.request.user.is_staff:
            return Appointment.objects.all()
        else:
            return Appointment.objects.filter(author=self.request.user)


class EmpListView(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'emppatientviewappointments.html'

    def get_queryset(self):
        if self.request.user.is_staff:
            return Appointment.objects.all()
        else:
            return Appointment.objects.filter(author=self.request.user.is_patient)


class AppointmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Appointment
    template_name = 'appointment_delete.html'
    success_url = 'EmpListView'


def AddAppointment(request):
    submitted = False
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return HttpResponseRedirect('/appointment?submitted=True')
    else:
        form = AppointmentForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'addappointments.html', {'form': form, 'submitted': submitted})

class empAppEdit(LoginRequiredMixin, UpdateView):
    model = Appointment
    fields = ['doctorname', 'doctoremail', 'patientname', 'patientemail', 'symptoms', 'prescription',
              ]
    template_name = 'employee_appointment.html'
    success_url = reverse_lazy('employee_homepage')
