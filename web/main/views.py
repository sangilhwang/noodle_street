from django.shortcuts import render
from single_pages.models import Restraunt

# Create your views here

def main(request):
    lists = Restraunt.objects.all()
    context = {
        "lists" : lists,
        }
    return render(request, 'main/main.html', context)

def restaurant_list(request, gu):
    restaurants = Restraunt.objects.filter(address_gu=gu)
    keyword = request.GET.get("keyword", None)
    
    if keyword :  
        restaurant_keyword = Restraunt.objects.filter(name__contains = keyword)
    else : # keyword가 주어지지않아, None이 할당된 경우
        restaurant_keyword = Restraunt.objects.none() # 빈 QuerySet을 할당
    context = {
        "restaurants":restaurants,
        'gu':gu,
        "restaurant_keyword" : restaurant_keyword,
    }
    return render(request, 'main/restaurant_list.html', context)

def test(request):
    return render(request, 'main/test1.html')