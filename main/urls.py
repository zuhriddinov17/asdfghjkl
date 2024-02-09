from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name="index_url"),
    path('search-patient/', search_patient_view, name='search_patient_url'),
    path('patient-single/int:pk>/', patient_single_view, name='patient_single_url'),
    path('doctor-single/<int:pk>/', doctor_details_view, name='doctor_details_url')
]