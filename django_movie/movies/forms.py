from django import forms

from .models import Reviews


class ReviewForm(forms.ModelForm):
    # форма за коментарите

    class Meta:
        model = Reviews
        fields = ('name', 'text')
