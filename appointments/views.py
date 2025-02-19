# clinic-booking/appointments/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # Make sure this is imported
from django.core.exceptions import ObjectDoesNotExist
from .forms import AppointmentForm
from .models import Appointment

@login_required
def book_appointment(request):
    try:
        profile = request.user.profile
    except ObjectDoesNotExist:
        profile = None

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        print("POST data received:", request.POST)  # Debug
        if form.is_valid():
            print("Form is valid")  # Debug
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.first_name = request.user.first_name
            appointment.last_name = request.user.last_name
            if profile:
                appointment.course = profile.course
                appointment.block = profile.block
            appointment.save()
            print("Appointment saved:", appointment.id)  # Debug
            return redirect('appointment_success')
        else:
            print("Form errors:", form.errors)  # Debug
    else:
        initial_data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }
        if profile:
            initial_data.update({
                'course': profile.course,
                'block': profile.get_block_display(),
            })
        form = AppointmentForm(initial=initial_data)
    return render(request, 'appointments/book_appointment.html', {'form': form})

@login_required
def appointment_success(request):
    return render(request, 'appointments/appointment_success.html')

@login_required
def appointment_history(request):
    appointments = Appointment.objects.filter(user=request.user).order_by('-date')
    return render(request, 'appointments/appointment_history.html', {
        'appointments': appointments
    })