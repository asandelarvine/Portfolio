from django.urls import path

from . import views


urlpatterns =[

    path("",views.index,name="index"),
    path("profile",views.profile,name="profile"),
    path("projects",views.projects,name="projects"),
    path("experiences",views.experiences,name="experiences"),
    path("blogs",views.blogs,name="blogs"),
    


]