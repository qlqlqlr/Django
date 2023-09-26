from django.shortcuts import render
import random
# Create your views here.

def certification1(request):
    name = 'lee happy'
    age = range(25,31)
    grade = ['a','b','c','s']
    pickage = random.choice(age)
    pickgr = random.choice(grade)

    context = {
        'name': name,
        'age': pickage,
        'grade': pickgr,
    }
    return render(request, 'articles/certification1.html', context)


def certification2(request):
    name = 'park happy'
    age = range(25,31)
    grade = ['a','b','c','s']
    pickage = random.choice(age)
    pickgr = random.choice(grade)

    context = {
        'name': name,
        'age': pickage,
        'grade': pickgr,
    }
    return render(request, 'articles/certification2.html', context)

def certification3(request):
    name = 'kim happy'
    age = range(25,31)
    grade = ['a','b','c','s']
    pickage = random.choice(age)
    pickgr = random.choice(grade)

    context = {
        'name': name,
        'age': pickage,
        'grade': pickgr,
    }
    return render(request, 'articles/certification3.html', context)