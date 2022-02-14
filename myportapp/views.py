from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from .models import Project, Blog, Skill,Experience,Profile
# Create your views here.
from .forms import NameForm

from django.conf import settings
from django.core.mail import send_mail

def index(request):
    current_user = request.user
    if request.method == "POST":
        
        form=NameForm(request.POST,request.FILES)

        if form.is_valid():
            comment=form.save(commit=False)
            comment.user=current_user
            
            comment.save()
        return HttpResponseRedirect('/')
    else:
        form=NameForm()

    template = loader.get_template("./myportfolio/index.html")
    projects = Project.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all().order_by('-start_date')[:5]
    profile = Profile.objects.all().order_by('-id')
    form = NameForm()
    context = {'projects': projects, 'skills': skills, 'form': form,'experiences':experiences,'profile':profile}
    return HttpResponse(template.render(context, request))

def profile(request):
    profile = Profile.objects.all().order_by('-id')
    return render(request, "myportfolio/index.html", {"profile":profile})


def experiences(request):
    return HttpResponse("you are in experience page")


def blogs(request):
    template = loader.get_template("myportfolio/blog.html")
    blogs = Blog.objects.all().order_by('-published_on')
    context = {'blogs': blogs}
    return HttpResponse(template.render(context, request))



def projects(request):
    return HttpResponse("you are in projects pages")