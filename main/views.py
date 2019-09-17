from django.shortcuts import render, redirect
from .forms import NewAppointmentForm

# Create your views here.


def home_page_view(request, *args, **kwargs):  # *args, **kwargs
    return render(request, 'home.html', {})


def make_appointment_view(request, *args, **kwargs):  # *args, **kwargs
    if request.method == 'POST':
        form = NewAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'hospital': form.cleaned_data.get('hospital'),
                'when': form.cleaned_data.get('when'),
                'first_name': form.cleaned_data.get('first_name'),
                'last_name': form.cleaned_data.get('last_name'),
                'insurance_id': form.cleaned_data.get('insurance_id')
            }
            return render(request, 'appointment_detail.html', context)
    form = NewAppointmentForm
    return render(request, 'appointment.html', context={'form': form})
