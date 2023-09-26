from django.shortcuts import render

# Create your views here.
def price(request, thing, cnt):
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}
    pri = 0
    
    if thing in product_price:
        pri = product_price[thing] * cnt
        context = {
            'thing' : thing,
            'cnt' : cnt,
            'pri' : pri,
            'yorn' : 1
        }
    else:

        context = {
            'thing' : thing,
            'yorn' : 0
        }

    return render(request, 'prices/price.html', context)