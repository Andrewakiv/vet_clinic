# Vet Clinic

Simple site for vet clinic with blog, services, orders, profile etc...

## Quickstart

    sudo apt get update
    git clone https://github.com/Andrewakiv/vet_clinic.git
    cd src
      
    python3 -m venv venv   
    source venv/bin/activate
    pip3 install -r requirements.txt 
    
    cp .env.template .env
    
Run the app locally:

    python3 manage.py runserver 0.0.0.0:8000

Run the app with gunicorn:

    gunicorn project.wsgi -b 0.0.0.0:8000