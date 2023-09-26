import random
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'name': 'Jane',
    }
    return render(request, 'articles/index.html', context)

def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육',]
    picked = random.choice(foods)
    empth_list = []
    context = {
        'foods' : foods,
        'picked' : picked,
        'empty_list' : empth_list,
    }
    return render(request, 'articles/dinner.html', context)

def search(request):
    return render(request, 'articles/search.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    # 사용자로 부터 요청을 받아서
    # 요청에서 사용자 입력 데이터를 찾아 
    # context에 저장 후 catch 템플릿에 출력
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request, 'articles/catch.html', context)

def greeting(request, name):
    context = {
        'name': name,
    }
    return render(request, 'articles/greeting.html', context)

def detail(request, num):
    context = {
        'num': num,
    }
    return render(request, 'articles/detail.html', context)


def fruits(request):
    
    fruit_list = ["귤","딸기","사과","감","바나나","파인애플","구아바", "복숭아", "망고스틴"]
    hate = ["사과","구아바"]

    context = {
        'fruit_list' : fruit_list,
        'hate' : hate,
    }
    return render(request, 'articles/fruit.html', context)


def calculation(request):

    return render(request, 'articles/calculation.html')

def result(request):
    # 사용자로 부터 요청을 받아서
    # 요청에서 사용자 입력 데이터를 찾아 
    # context에 저장 후 catch 템플릿에 출력
    num1 = int(request.GET.get('num1'))
    num2 = int(request.GET.get('num2'))
    result2 = num1 * num2
    result3 = num1 - num2
    if num2 == 0:
        result4 = 0
    else:
        result4 = num1 / num2

    context = {
        'num1' : num1,
        'num2' : num2,
        'result2' : result2,
        'result3' : result3,
        'result4' : result4
    }
    return render(request, 'articles/result.html', context)