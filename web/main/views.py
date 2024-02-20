from django.shortcuts import render
from single_pages.models import Restraunt
from users.models import User

# Create your views here

def main(request):
    lists = Restraunt.objects.all()
    context = {
        "lists" : lists,
        }
    return render(request, 'main/main.html', context)

# def restaurant_list(request, gu):
#     restaurants = Restraunt.objects.filter(address_gu=gu)
#     keyword = request.GET.get("keyword", None)
#     # 검색기능 구현
#     if keyword :  
#         restaurant_keyword = Restraunt.objects.filter(name__contains = keyword)
#     else : # keyword가 주어지지않아, None이 할당된 경우
#         restaurant_keyword = Restraunt.objects.none() # 빈 QuerySet을 할당
#     context = {
#         "restaurants":restaurants,
#         'gu':gu,
#         "restaurant_keyword" : restaurant_keyword,
#     }
#     return render(request, 'main/restaurant_list.html', context)

def restaurant_list(request, gu):
    restaurants = Restraunt.objects.filter(address_gu=gu)
    # 주차 여부 체크박스가 선택되었는지 확인
    parking_option = request.GET.get('parking', None)
    
    # 검색어가 입력되었는지 확인
    keyword = request.GET.get('keyword', None)

    if keyword:
        # 키워드로 검색한 경우
        restaurant_keyword = Restraunt.objects.filter(name__contains = keyword)
        if parking_option == 'on':
            # 주차 가능 여부 체크박스가 선택된 경우
            restaurant_keyword = restaurant_keyword.filter(parking=True, address_gu=gu)
        context = {
            'restaurant_keyword': restaurant_keyword,
            'parking_option' : parking_option,
            'keyword': keyword,
            'gu':gu,
        }
        return render(request, 'main/restaurant_list.html', context)
    
    elif parking_option == 'on':
        # 주차 가능 여부 체크박스만 선택한 경우
        restaurants = Restraunt.objects.filter(parking=True, address_gu=gu)
        context = {
            'restaurants': restaurants,
            'parking_option' : parking_option,
            'gu':gu,
        }
        return render(request, 'main/restaurant_list.html', context)
    else:
        # 아무런 필터가 없는 경우
        restaurants = Restraunt.objects.filter(address_gu=gu)
        context = {
            'restaurants': restaurants,
            'gu':gu,
        }
        return render(request, 'main/restaurant_list.html', context)


def test(request):
    return render(request, 'main/test1.html')