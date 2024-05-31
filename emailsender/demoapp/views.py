from django.shortcuts import render

# Create your views here.
def sendanemail(request):
    return render(
        request,
        'email.html',
        {
            'title':'send an email'
        }
    )