from django import forms

class RatingReviewForm(forms.Form):
    rating = forms.CharField(max_length=128)
    review = forms.CharField(max_length=128)