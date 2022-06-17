from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import requests
from movie.models import Movie


def movie(request):

    movie = Movie.objects.all()
    
    context = {
        'movie' : movie
    }

    return render(request, 'movie/home.html', context)


TMDB_API_key = "06436ebd388cbc01d6afabd394c2fd72"


def search(request):

    query = request.GET.get('q')

    results = []
    if query:

        data = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_key}&language=en-US&page=1&include_adult=false&query={query}")


    else:
        return HttpResponse('Please enter a search query')

    content = {
        'data' : data.json()
    }

    return render(request, 'movie/results.html', content)

def index(request):
    return render(request, 'movie/index.html')


def movie_detail(request, movie_id):

    
    data = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_key}&language=en-US")

    content= {
        'data' : data.json()
    }

    if request.method == "POST":
        title = request.POST['title']
        year = request.POST['year']
        description = request.POST['description']
        review = request.POST['review']
        rating = request.POST['rating']
        image = request.POST['image']

        movie_info = Movie(title=title,year=year,description=description,review=review,rating=rating,img_url=image)
        movie_info.save()
        return redirect('home')
    
    return render(request, 'movie/movie_detail.html', content)

def update_movie(request,pk):
    event = Movie.objects.get(id=pk)
   
    if request.method == "POST":
        event.rating = request.POST.get('rating')
        event.review = request.POST.get('review')
        event.save()
        return redirect('home')

    context={
        'event' : event,
    }
    return render(request, "movie/update_movie.html", context)
   

def delete_movie(request,pk):
    event = Movie.objects.get(id=pk)
    event.delete()
    return redirect('home')