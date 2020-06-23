from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView

from dq.models import Appointment,Patient
from dq.forms import AppointmentForm,PatientForm

from datetime import datetime, timedelta ,date

def appointment_list(request, patient_id=None):
    # return HttpResponse('予約の一覧')
    is_patient = False
    if patient_id:
        is_patient = True
        patient = get_object_or_404(Patient, pk=patient_id)
        appointments = patient.appointments.all().order_by('id')
    else :
        appointments = Appointment.objects.all().order_by('id')

    return render(request,
    'dq/appointment_list.html',
    {
        'appointments':appointments,
        'is_patient':is_patient,
    })

def appointment_edit(request, appointment_id=None):
    # return HttpResponse('予約の編集')
    if appointment_id:
        appointment = get_object_or_404(Appointment, pk=appointment_id)
    else:
        appointment = Appointment()

    if request.method == 'POST':
        form = AppointmentForm(request.POST,instance=appointment)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.save()
            return redirect('dq:appointment_list')
    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'dq/appointment_edit.html',dict(form=form, appointment_id=appointment_id))

def appointment_del(request, appointment_id):
    # return HttpResponse('予約の削除')
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    appointment.delete()
    return redirect('dq:appointment_list')

class ApointmentList(ListView):
    """患者が持つ予約のリスト"""
    context_object_name = 'appointments'
    template_name = 'dq/patient_appointments_list.html'
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        patient = get_object_or_404(Patient, pk=kwargs['patient_id'])
        appointments = patient.appointments.all().order_by('id')
        self.object_list = appointments

        context = self.get_context_data(object_list=self.object_list, patient=patient)
        return self.render_to_response(context)

def patient_list(request):
    # return HttpResponse('TEST')
    patients = Patient.objects.all().order_by('id')
    return render(request,
    'dq/patient_list.html',
    {'patients':patients})

def patient_edit(request, patient_id=None):
    # return HttpResponse('TEST')
    if patient_id:
        patient = get_object_or_404(Patient, pk=patient_id)
    else:
        patient = Patient()

    if request.method == 'POST':
        form = PatientForm(request.POST,instance=patient)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.save()
            return redirect('dq:patient_list')
    else:
        form = PatientForm(instance=patient)

    return render(request, 'dq/patient_edit.html',dict(form=form, patient_id=patient_id))

def patient_del(request):
    return HttpResponse('TEST')

def grid(request):
    today = date.today()
    
    time_str_start = "7:00"
    time_str_end = "23:59"
    time_start = datetime.strptime(time_str_start, '%H:%M')
    time_end = datetime.strptime(time_str_end, '%H:%M')
    time_unit = timedelta(minutes=5) #5分刻み

    time_current = time_start
    times = []
    while time_current <= time_end:
        times.append(time_current.strftime('%H:%M'))
        time_current += time_unit

    dates = []
    for i in range(12):
        date_current = today + timedelta(days=i)
        dates.append({
            'year':date_current.strftime('%y'),
            'month':date_current.strftime('%m'),
            'day':date_current.strftime('%d'),
            'week':date_current.strftime('%a'),
        })
            
    return render(request,
    'dq/grid2.html',
    {
        'dates':dates,
        'times':times,
        'cellsOfColumn':times.count,
    })