from django.shortcuts import render

from .models import Home, Department, Teacher, Program

def home(request):
    page = Home.objects.first()
    return render(request, "faculty/home.html", {"home": page})

def departments(request):
    cafedry = Department.objects.all()
    return render(request, "faculty/departments.html",{"departments":cafedry})

def department_id(request, id):
    cafedra = Department.objects.get(id=id)
    teachers = Teacher.objects.filter(department=cafedra)
    spc = Program.objects.filter(department=cafedra)
    context ={
        "department":cafedra,
        "teachers":teachers,
        "programs":spc,
    }
    return render(request, "faculty/detail.html", context)

def programs(request):
    prog = Program.objects.all()
    return render(request,"faculty/programs.html",{"programs":prog})


def prog_id(request, id):
    prog_id = Program.objects.get(id=id)
    return render(request, "faculty/prog_detail.html", {"program":prog_id})