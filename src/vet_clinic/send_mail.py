import os
import sys
import django
from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ["DJANGO_SETTINGS_MODULE"] = "project.settings"

django.setup()

from accounts.models import Profile
from vet_clinic.models import Post

users_with_subscribe = Profile.objects.filter(send_mail=True)
latest_posts = Post.objects.all()[:3]

for user in users_with_subscribe:

    subject = f"Read latest posts at Best.Pet"
    message = f"Read {latest_posts[0]}, {latest_posts[1]} and {latest_posts[2]}"
    send_mail(subject, message, EMAIL_HOST_USER,
              [user.user.email])

