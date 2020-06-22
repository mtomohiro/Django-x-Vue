from django.contrib import admin
from dq.models import Patient,Appointment

# 最もシンプルな形
# admin.site.register(Patient)
# admin.site.register(Appointment)

# 患者の選択画面が変わる。
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id','name','birth',)
    list_display_links = ('id','name',)

admin.site.register(Patient,PatientAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id','bookDateTime','patient',)
    list_display_links = ('id','bookDateTime',)
    # よくわからない
    # raw_id_fields = ('patient',)

admin.site.register(Appointment,AppointmentAdmin)