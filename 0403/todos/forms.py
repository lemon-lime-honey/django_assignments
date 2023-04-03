from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '제목을 입력하세요'},
        ),
        label='제목'
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '내용을 입력하세요'},
        ),
        label='내용'
    )
    priority = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'min': 1, 'max': 5, 'value': 3},
        ),
        label='우선순위'
    )
    deadline = forms.DateField(
        widget=forms.DateInput(
            format=('%Y-%m-%d'), 
            attrs={'type': 'date',
                   'class': 'form-control'},
        ),
        label='마감기한'
    )

    class Meta:
        model = Todo
        fields = ('title', 'content', 'priority', 'deadline')