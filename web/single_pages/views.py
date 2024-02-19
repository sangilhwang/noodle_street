from django.shortcuts import render,redirect, get_object_or_404
from single_pages.models import Restraunt, RestrauntMenu
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse

# Create your views here.

def detail(request, restaurant_id):
    restaurant = get_object_or_404(Restraunt, id=restaurant_id)
    # restaurant_menu = RestrauntMenu.objects.filter(id=restaurant_id)
    restaurant_menu = RestrauntMenu.objects.filter(restraunt_pk_id=restaurant_id)    
    context = {"restaurant":restaurant,
               "restaurant_menu" : restaurant_menu,
    }
    return render(request, 'single_pages/restaurant_detail.html', context)

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