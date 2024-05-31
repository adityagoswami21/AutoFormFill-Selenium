from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from dotenv import load_dotenv
import os
load_dotenv()

# Create your views here.
def sendanemail(request):
    if request.method == "POST":
        to = request.POST.get('toemail')
        content = request.POST.get('content')
        # print(to,content)
        EmailMessage(
            "Python (Selenium) Assignment- Aditya Goswami",
            content,
            settings.EMAIL_HOST_USER,
            [to],
            cc=[os.getenv("EMAIL_CC")],
        )
        return render(
            request,
            'email.html',
            {
                'title':'send an email'
            }
        )
    else:
        return render(
            request,
            'email.html',
            {
                'title':'send an email'
            }
        )