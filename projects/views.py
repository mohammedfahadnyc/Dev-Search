import random

from django.shortcuts import render, redirect
from django.http import HttpResponse
from projects.models import Project
from projects.forms import ProjectForm
# Create your views here.


def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request,'projects/projects.html',context)

def project(request,pk):
    projectobj = Project.objects.get(id=pk)
    tags = projectobj.tags.all()
    context = {"project":projectobj,'tags':tags}
    # context = {'main_val' : pk, 'val' : random.randint(89,457) }
    return render(request,'projects/single-project.html',context)

def createProject(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create-project')

    context = {'form':form}
    return render(request,'projects/project-form.html',context)

def updateProject(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {"form":form}
    return render(request,"projects/project-form.html",context)



def deleteProject(request,pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('projects')
    context = {'project_name':project.title}
    return render(request, "projects/delete-project.html",context)