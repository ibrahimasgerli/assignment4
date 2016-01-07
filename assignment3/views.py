from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from new_assignment3.forms import *
from django.http import HttpResponseRedirect
from assignment3.models import *
from django.shortcuts import RequestContext
def addTeacher(request):
    if request.method=='POST':
        form=Teacher(request.POST)
        if form.is_valid():
            a=Teacher(first_name=form.cleaned_data["first_name"],
                      last_name=form.cleaned_data["last_name"],
                      office_details=form.cleaned_data["office_details"],
                      phone=form.cleaned_data["phone"],
                      email=form.cleaned_data["email"])
            a.save()
            return HttpResponseRedirect('/all_teachers/')
    else:
        form=Teacher()
    return render_to_response('addteacher.html',{'form':form},RequestContext(request))

def all_teachers(request):
    return render_to_response('teachers.html',
                              {'teacher_list':Teacher.objects.all()})



def addStudent(request):
    if request.method=='POST':
        form=Student(request.POST)
        if form.is_valid():
            a=Student(first_name=form.cleaned_data["first_name"],
                      last_name=form.cleaned_data["last_name"],
                      email=form.cleaned_data["email"])
            a.save()
            return HttpResponseRedirect('/all_students/')
    else:
        form=Student()
    return render_to_response('addstudent.html',{'form':form},RequestContext(request))

def all_students(request):
    return render_to_response('students.html',
                              {'student_list':Student.objects.all()})


def addCourses(request):
    if request.method=='POST':
        form=Course(request.POST)
        if form.is_valid():
            a=Course(name=form.cleaned_data["name"],
                     code=form.cleaned_data["code"],
                     classroom=form.cleaned_data["classroom"],
                     times=form.cleaned_data["times"])
            a.save()
            return HttpResponseRedirect('/all_courses/')
    else:
        form=Course()
    return render_to_response('addcourse.html',{'form':form},RequestContext(request))

def all_courses(request):
    return render_to_response('courses.html',
                              {'course_list':Course.objects.all()})
