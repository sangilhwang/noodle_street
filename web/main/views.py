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
    context = {
        "restaurants":restaurants,
        'gu':gu,
    }
    return render(request, 'main/restaurant_list.html', context)
