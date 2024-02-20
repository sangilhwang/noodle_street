from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from single_pages.models import Restraunt, RestrauntReview, RestrauntMenu
from single_pages.forms import ReviewForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def detail(request, restaurant_id):
    restaurant = get_object_or_404(Restraunt, id=restaurant_id)
    reviews = RestrauntReview.objects.filter(restraunt_pk_id=restaurant_id)
    reviewform = ReviewForm()
    restaurant_menu = RestrauntMenu.objects.filter(restraunt_pk_id=restaurant_id)
    #restaurant = Restraunt.objects.get(id=restaurant_id)
    context = {
        'restaurant':restaurant,
        'reviewform' : reviewform,
        'reviews' : reviews,
        'restaurant_menu' : restaurant_menu,
    }
    return render(request, 'single_pages/restaurant_detail.html', context)

@require_POST
def review_add(request, restaurant_id):

    if request.user.is_authenticated:

        form = ReviewForm(data=request.POST)

        print("아는 사람이야")

        if form.is_valid():
            review = form.save(commit=False)

            review.user_pk = request.user
            
            review.save()

            print("맞는 양식이야")

        url_next = request.GET.get("next") or reverse("single_pages:detail", kwargs={'restaurant_id': restaurant_id})

        return HttpResponseRedirect(url_next)
    
    return redirect("users:login")

@require_POST
def review_delete(request, restaurant_id, review_id):
    review = RestrauntReview.objects.get(id=review_id)

    if review.user_pk == request.user:
        review.delete()

        url_next = reverse("single_pages:detail", kwargs={'restaurant_id' : restaurant_id})

        return redirect(url_next)
    
    # restaurant_menu = RestrauntMenu.objects.filter(id=restaurant_id)
    # restaurant_menu = RestrauntMenu.objects.filter(restraunt_pk_id=restaurant_id)    
    # context = {"restaurant": restaurant,
    #            "restaurant_menu" : restaurant_menu,
    # }
    # return render(request, 'single_pages/restaurant_detail.html', context)

# 좋아요 구현
def restaurant_like(request, restaurant_id):
    restaurant = Restraunt.objects.get(id=restaurant_id)
    user = request.user # request를 한 유저

    if request.user.is_authenticated:
        # 사용자가 "좋아요를 누른 Restaurant 목록"에 "좋아요 버튼을 누른 Restaurant"이 존재한다면
        if user.like_restaurants.filter(id=restaurant.id).exists():
            # 좋아요 목록에서 삭제 (좋아요 해제)
            user.like_restaurants.remove(restaurant)

        # 존재하지 않는다면 좋아요 목록에 추가
        else : 
            user.like_restaurants.add(restaurant)
        
        # next로 값이 전달되었다면 해당 위치로, 전달되지 않았다면 레스토랑 위치로 이동
        url_next = request.GET.get("next") or reverse("single_pages:detail", kwargs={'restaurant_id': restaurant_id})
        return HttpResponseRedirect(url_next)
    
    else:
        return redirect("users:login")
