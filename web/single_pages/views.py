from django.shortcuts import render,redirect, get_object_or_404
from single_pages.models import Restraunt

# Create your views here.

def detail(request, restaurant_id):
    restaurant = get_object_or_404(Restraunt, id=restaurant_id)  
    #restaurant = Restraunt.objects.get(id=restaurant_id)
    context = {
        'restaurant':restaurant,
    }
    return render(request, 'single_pages/restaurant_detail.html', context)