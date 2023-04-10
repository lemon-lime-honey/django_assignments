from django import forms
from .models import Album


class AlbumForm(forms.ModelForm):
    content = forms.CharField(
        label='내용',
        widget=forms.TextInput(
        attrs={
        'max_length': 20,
        'class': 'form-control',
        'placeholder': '내용을 입력하세요'
        }))
    image = forms.ImageField(
        label = '사진', 
        required=False,)
    class Meta:
        model = Album
        fields = ('content', 'image')