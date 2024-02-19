from django.shortcuts import render, redirect, get_object_or_404
from single_pages.models import Restraunt, RestrauntReview
from single_pages.forms import ReviewForm

# Create your views here.

def detail(request, restaurant_id):
    restaurant = get_object_or_404(Restraunt, id=restaurant_id)
    reviews = RestrauntReview.objects.filter(restraunt_pk_id=restaurant_id)
    reviewform = ReviewForm()
    #restaurant = Restraunt.objects.get(id=restaurant_id)
    context = {
        'restaurant':restaurant,
        'reviewform' : reviewform,
        'reviews' : reviews
    }
    return render(request, 'single_pages/restaurant_detail.html', context)

def review_add(request):
    pass