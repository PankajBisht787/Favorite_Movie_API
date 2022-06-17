from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie, name = 'home'),
    path('search_movie', views.index, name = 'index'),
    path('search/', views.search, name = 'search'),
    path('movie/<int:movie_id>/', views.movie_detail ,  name="movie_detail"),
    path('update_movie/<int:pk>/', views.update_movie ,  name="update_movie"),
    path('delete_movie/<int:pk>/', views.delete_movie ,  name="delete_movie"),
]