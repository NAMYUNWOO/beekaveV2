from django import forms
from reviewPage.models import reviewMovie

class movieReviewForm(forms.ModelForm):

    class Meta:
        model = reviewMovie
        fields = '__all__'
