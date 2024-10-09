import datetime
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # passing dynamic data from views to template
    isActive = True
    if request.method == 'POST':
        check = request.POST.get('check')
        print(check)
        if check is None: isActive=False
        else: isActive=True
    date = datetime.datetime.now()
    name = 'Learn Code With Durgesh'
    list_of_programs = [
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime numbers from 1 to 100',
        'WAP to print pascals triangle',
    ]

    student = {
        "student_name":"Rahul",
        "student_college":"xyz",
        "student_city":"Lucknow"
    }

    data = {
        "date": date,
        "isActive" : isActive,
        "name" : name,
        "list_of_programs" : list_of_programs,
        "student": student
    }

    return render(request,"home.html",data)

def about(request):
    return render(request,'about.html',{})

def services(request):
    return render(request,'services.html',{})