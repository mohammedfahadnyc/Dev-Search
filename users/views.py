from django.shortcuts import render
from users.models import Profile
# Create your views here.

def profiles(request):
    profiles = Profile.objects.all()
    context = {"profiles":profiles}
    return render (request,'users/profiles.html',context)

def userprofile(request,pk):
    profile = Profile.objects.get(id=pk)
    top_skills = profile.skill_set.exclude(description = "")
    other_skills = profile.skill_set.filter(description="")
    projects = profile.project_set.all()
    context = {"profile":profile,'t_skills':top_skills,"o_skills":other_skills,"projects":projects}
    return render(request,'users/user-profile.html',context)



