from django.shortcuts import render
# Create your views here.

def first(request):
    message = request.GET.get('message', 'nothing')
    context = {
        'message' : message,
    }
    return render(request, 'throw/first.html', context)

def second(request):
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request, 'throw/second.html', context)


def third(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    arr = []
    arr.append(message)
    arr.append(message2)
    
    context = {
        'message' : arr,
    }
    return render(request, 'throw/third.html', context)