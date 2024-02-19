from django import forms
from single_pages.models import RestrauntReview

class ReviewForm(forms.ModelForm):
    class Meta:
        model = RestrauntReview
        fields = [
            "restraunt_pk",
            "comment",            
        ]
        widgets = {"comment": forms.Textarea(attrs={"placeholder": "리뷰 작성..."})}