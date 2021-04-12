from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .models import Doctor, Patient, Appointment, Receptionist

from hospital.forms import CustomUserCreationForm


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'templates/contact.html', {})


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
            return redirect('admin_homepage')
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
                return redirect('admin_homepage')
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
            return render(request, 'login.html', {'form': form, 'info': info})
    else:
        form = AuthenticationForm(request.POST)
        return render(request, 'login.html', {'form': form})


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
            return redirect('patient_homepage')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def admin_homepage(request):
    return render(request, 'admin_homepage.html')


def patient_homepage(request):
    return render(request, 'patient_homepage.html')


def receptionist_homepage(request):
    return render(request, 'receptionist_homepage.html')


def doctor_homepage(request):
    return render(request, 'doctor_homepage.html')
