from django import forms
from localmedia.models import Post,Comment, Image
class Commentform(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ['comment']

class ImageForm(forms.ModelForm): 
    class Meta: 
        model = Image
        fields = ['post_image']


