from django.shortcuts import render

# Create your views here.

def calculator(request, num1, num2):
    num1 = num1
    num2 = num2
    if num2 != 0:
        dev = num1 / num2
    else:
        dev = '계산할 수 없습니다'

    context = {
        'num1' : num1,
        'num2' : num2,
        'hab' : num1 + num2,
        'cha' : num1 - num2,
        'gob' : num1 * num2,
        'dev' : dev,
    }
    return render(request, 'calculator/calculator.html', context)