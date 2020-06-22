from django.urls import path
from api import views

app_name = 'api'
urlpatterns = [
    # 書籍
    path('v1/patients/', views.patient_list, name='patient_list'),   # 一覧
]