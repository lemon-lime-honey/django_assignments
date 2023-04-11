from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ReviewForm, CommentForm
from .models import Review, Comment


def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save()
            return redirect('reviews:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'reviews/create.html', context)


def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comments = review.comment_set.all()
    form = CommentForm()
    context = {
        'review': review,
        'comments': comments,
        'form': form,
    }
    return render(request, 'reviews/detail.html', context)


@login_required
def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    review.delete()
    return redirect('reviews:index')


@login_required
def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect('reviews:detail', review.pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        'review': review,
        'form': form,
    }
    return render(request, 'reviews/update.html', context)


@login_required
def comment_create(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.review = review
        comment.save()
        return redirect('reviews:detail', review.pk)
    context = {
        'review': review,
        'form': form,
    }
    return render(request, 'reviews/detail.html', context)


def comment_delete(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('reviews:detail', review_pk)