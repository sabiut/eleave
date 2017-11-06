from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.conf import settings

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.contrib import  auth
from eLeave.models import newleave

#views.py

# Create your views here.

def sending_email(request):
    to_emails = [u.email for u in User.objects.filter(username__in=['testuser'])]
    send_mail("RBV Leave Application Email Testing", "You have received a leave application form. Please login to the leave system to Authorize the leave.\nhttp://10.0.142.35:8000/eLeave",
    "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
    return render_to_response('thankyou.html')

