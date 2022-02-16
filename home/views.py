from django.shortcuts import render
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from .tools.time import intro
from .models import Interest, Work, Question, Developer
from django.conf import settings
# Create your views here.

def homeView(request):
    interests = Interest.objects.all()
    works = Work.objects.all()
    questions = Question.objects.all()
    developers = Developer.objects.all()

    context = {
        'show_intro': True,
        'interests': interests,
        'works': works,
        'questions': questions,
        'developers': developers,
    }
    # put return value as elements of context
    context = dict(context, **intro())

    return render(request, 'home/home.html', context)


def sendMail(request):
    if (request.method == 'POST'):
        print(request.POST)

        subject = request.POST['subject']
        message = "You have one message from @" + \
            request.POST['name'] + "\n\n" + request.POST['email'] + \
            request.POST['email_postfix'] + "\n\n" + request.POST['message'] + \
            "\n\nHorizon Team\nuw.horizon.team@gmail.com\n" + \
            "University of Washington Tacoma 1900 Commerce Street\nTacoma, WA 98402-3100"
            
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            ['quminzhi@gmail.com'],   # to whom
            fail_silently=False,
        )
        
        return redirect('home')
 