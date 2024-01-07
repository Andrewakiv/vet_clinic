from django.urls import path
from . import views

app_name = 'vet_clinic'

urlpatterns = [
    path('', views.home, name='header_content'),
]
