from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete',),
    path('<int:article_pk>/like/', views.article_like, name='article_like',),
    path('<int:article_pk>/comments/<int:comment_pk>/like/', views.comment_like, name='comment_like'),
]