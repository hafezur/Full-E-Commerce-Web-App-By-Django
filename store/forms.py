from django import forms 
from.models import CommentAndReview

class commentAndReviewForm(forms.Form):
      write_comment = forms.CharField(
        max_length=1000,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your comment', 'class': 'form-control'})
         )
      ratings = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Rating', 'class': 'form-control'})
         )