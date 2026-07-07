from django import forms
from .models import SeatBooking, MovieReview


class BookingForm(forms.ModelForm):
    class Meta:
        model = SeatBooking
        fields = [
            "customer_name",
            "customer_phone",
        ]


class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(
        choices=[
            (1, "⭐"),
            (2, "⭐⭐"),
            (3, "⭐⭐⭐"),
            (4, "⭐⭐⭐⭐"),
            (5, "⭐⭐⭐⭐⭐"),
        ]
    )

    class Meta:
        model = MovieReview
        fields = [
            "reviewer_name",
            "rating",
            "comment",
        ]