from django.contrib import admin
from django.urls import path, include
from patient_app import views
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('patientapi', views.PatientModelViewSet, basename='patient')


urlpatterns = [
    path('', views.index, name='home'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('update_patient/', views.update_patient, name='update_patient'),
    path('edit_patient/', views.edit_patient, name='edit_patient'),
    path('update_patient/<int:pk>', views.update_patient, name='update_patient'),
    path('delete_patient/<int:pk>', views.delete_patient, name='delete_patient'),
    path('', include(router.urls))

]
