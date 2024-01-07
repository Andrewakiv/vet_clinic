from django.shortcuts import render


def home(request):
    return render(request, 'vet_clinic/index.html')

