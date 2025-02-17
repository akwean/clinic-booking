# clinic-booking/appointments/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .forms import AppointmentForm

@login_required
def book_appointment(request):
    try:
        profile = request.user.profile
    except ObjectDoesNotExist:
        profile = None

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.first_name = request.user.first_name
            appointment.last_name = request.user.last_name
            if profile:
                appointment.course = profile.course
                appointment.block = profile.block
            appointment.save()
            return redirect('appointment_success')
    else:
        initial_data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }
        if profile:
            initial_data.update({
                'course': profile.course,
                'block': profile.block,
            })
        form = AppointmentForm(initial=initial_data)
    return render(request, 'appointments/book_appointment.html', {'form': form})

@login_required
def appointment_success(request):
    return render(request, 'appointments/appointment_success.html')