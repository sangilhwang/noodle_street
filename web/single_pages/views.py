from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from single_pages.models import Restraunt, RestrauntReview
from single_pages.forms import ReviewForm
from django.http import HttpResponseRedirect
from django.urls import reverse

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

@require_POST
def review_add(request, restaurant_id):

    if request.user.is_authenticated:

        form = ReviewForm(data=request.POST)

        if form.is_valid():
            review = form.save(commit=False)

            review.user_pk = request.user
            
            review.save()

        url_next = request.GET.get("next") or reverse("single_pages:detail", kwargs={'restaurant_id': restaurant_id})

        return HttpResponseRedirect(url_next)
    
    return redirect("users:login")

# next로 값이 전달되었다면 해당 위치로, 전달되지 않았다면 레스토랑 위치로 이동
    