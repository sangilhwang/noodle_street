from django.db import models

# Create your models here.

class Restraunt(models.Model):
    name = models.CharField("이름", max_length=30)
    address = models.CharField("주소", max_length=30)
    address_gu = models.CharField("구", max_length=5)
    mon_busi_time = models.CharField("월요일 영업시간", max_length=20)
    mon_break_time = models.CharField("월요일 휴식시간", max_length=20)
    mon_finish_time = models.TimeField("월요일 마감시간", auto_now=False)
    tue_busi_time = models.CharField("화요일 영업시간", max_length=20)
    tue_break_time = models.CharField("화요일 휴식시간", max_length=20)
    tue_finish_time = models.TimeField("화요일 마감시간", auto_now=False)
    wed_busi_time = models.CharField("수요일 영업시간", max_length=20)
    wed_break_time = models.CharField("수요일 휴식시간", max_length=20)
    wed_finish_time = models.TimeField("수요일 마감시간", auto_now=False)
    thu_busi_time = models.CharField("목요일 영업시간", max_length=20)
    thu_break_time = models.CharField("목요일 휴식시간", max_length=20)
    thu_finish_time = models.TimeField("목요일 마감시간", auto_now=False)
    fri_busi_time = models.CharField("금요일 영업시간", max_length=20)
    fri_break_time = models.CharField("금요일 휴식시간", max_length=20)
    fri_finish_time = models.TimeField("금요일 마감시간", auto_now=False)
    sat_busi_time = models.CharField("토요일 영업시간", max_length=20)
    sat_break_time = models.CharField("토요일 휴식시간", max_length=20)
    sat_finish_time = models.TimeField("토요일 마감시간", auto_now=False)
    sun_busi_time = models.CharField("일요일 영업시간", max_length=20)
    sun_break_time = models.CharField("일요일 휴식시간", max_length=20)
    sun_finish_time = models.TimeField("일요일 마감시간", auto_now=False)
    phone_no = models.CharField("연락처", max_length=15)
    parking = models.BooleanField("주차시설", initial=False)
    rating = models.FloatField("평점")
    rating_count = models.IntegorField("평점 수")
    image = models.ImageField("대표 이미지", upload_to=None)

class RestrauntMenu(models.Model):
    restraunt_pk = models.ForeignKey(Restraunt, verbose_name="음식점 id", on_delete=models.CASCADE)
    name = models.CharField("이름", max_length=30)
    price = models.IntegorField("가격")

class RestrauntReview(models.Model):
    restraunt_pk = models.ForeignKey(Restraunt, verbose_name="음식점 id", on_delete=models.CASCADE)
    user_pk = models.ForeignKey(User, verbose_name="유저 id", on_delete=models.CASCADE)
    comment = models.TextField("내용")