from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '제목을 입력하세요',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '내용을 입력하세요',
                'style': 'height: 10em;',
            }
        )
    )
    movie = forms.CharField(
        label='영화',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '영화 제목을 입력하세요',
            }
        )
    )
    image = forms.ImageField(
        label='사진',
        required=False,
    )

    class Meta:
        model = Review
        fields = ('title', 'content', 'movie', 'image',)


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='댓글',
        widget=forms.TextInput(
            attrs={
                'placeholder': '댓글 내용을 입력하세요',
            }
        )
    )
    class Meta:
        model = Comment
        fields = ('content',)