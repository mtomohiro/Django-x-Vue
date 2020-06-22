from django.urls import path
from dq import views

app_name = 'dq'
urlpatterns = [
    path('grid/',views.grid, name='grid'),
    path('appointment/',views.appointment_list, name='appointment_list'),
    path('appointment/<int:patient_id>/',views.appointment_list, name='appointment_list'),
    path('appointment/add/',views.appointment_edit, name='appointment_add'),
    path('appointment/mod/<int:appointment_id>/',views.appointment_edit, name='appointment_mod'),
    path('appointment/del/<int:appointment_id>/',views.appointment_del, name='appointment_del'),
    path('patient/',views.patient_list, name='patient_list'),
    path('patient/add/',views.patient_edit, name='patient_add'),
    path('patient/mod/<int:patient_id>/',views.patient_edit, name='patient_mod'),
    path('patient/del/<int:patient_id>/',views.patient_del, name='patient_del'),
]

