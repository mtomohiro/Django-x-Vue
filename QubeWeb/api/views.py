import json
from collections import OrderedDict
from django.http import HttpResponse
from dq.models import Appointment, Patient

def render_json_response(request, data, status=None):
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    callback = request.GET.get('callback')
    if not callback:
        callback = request.POST.get('callback')
    
    if callback:
        json_str = "%s(%s)" % (callback, json_str)
        response = HttpResponse(json_str, content_type='application/javascript; charset=UTF-8', status=status)
    else:
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=status)
        
    return response

def patient_list(request):
    patients = []
    for patient in Patient.objects.all().order_by('id'):
        appointments = []
        for appointment in patient.appointments.order_by('id'):
            appointment_dict = OrderedDict([
                ('id', appointment.id),
                ('test','test'),
                # ('bookDateTime',appointment.bookDateTime),
            ])
            appointments.append(appointment_dict)

        patient_dict = OrderedDict([
            ('id',patient.id),
            ('name',patient.name),
            ('appointments',appointments),
        ])
        patients.append(patient_dict)

    data = OrderedDict([ ('patient',patients) ])
    return render_json_response(request,data)