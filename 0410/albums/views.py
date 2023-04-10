from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import Album


def index(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('albums:index')
    form = AlbumForm()
    albums = Album.objects.all()
    context = {
        'albums': albums,
        'form': form,
        'iterator': range(10)
    }
    return render(request, 'albums/index.html', context)


def refresh(request):
    redirect('albums:index')