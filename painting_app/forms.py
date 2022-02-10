from django import forms
from .models import *
  
# class ImageForm(forms.ModelForm):
  
#     class Meta:
#         model = Painting_Images
#         fields = ['name', 'Main_Img']

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()