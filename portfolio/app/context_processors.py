from . models import *


def about(request):
    about = AboutMe.objects.first()
    intro = Intro.objects.first()
    exp=Experience.objects.all()
    skill=Skills.objects.all()
    portfolio=Portfolio.objects.all()
    

    return({
        'about':about,
        'intro':intro,
        'exp':exp,
        'skills':skill,
        'porfolio':portfolio

    })
