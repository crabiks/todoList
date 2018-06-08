from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie, PersonMovie, Person


def movie_list(request):
    movies = Movie.objects.all().order_by('-year')
    movies_asc = Movie.objects.all().order_by('rating')
    movies_des = Movie.objects.all().order_by('-rating')
    # return render(request, 'movies.html', {'movies': movies})
    if request.method == "GET":
        return render(request, 'movies.html', {
            'movies': movies
        })
    elif request.method == "POST":
        sorted = request.POST.get('sorted')
        request.session['sorted'] = sorted
        if sorted == '1':
            return render(request, 'movies.html', {
                'movies': movies_des
            })
        if sorted == '2':
            return render(request, 'movies.html', {
                'movies': movies_asc
            })
        if sorted == '0':
            return render(request, 'movies.html', {
                'movies': movies
            })


def movie_details(request, id):
    movie = Movie.objects.get(id=id)
    genre = movie.genre.all()
    role = PersonMovie.objects.filter(movie_id=id)
    return render(request, 'movie_details.html', {'movie': movie, 'genre': genre, 'role': role})


def persons(request):
    persons = Person.objects.all()
    return render(request, 'persons.html', {'persons': persons})


def person_edit(request, id):
    person = Person.objects.get(id=id)
    if request.method == "GET":
        return render(request, 'person_edit.html', {'person': person})
    if request.method == "POST":
        name = request.POST['first_name']
        surename = request.POST.get("last_name")
        person.first_name = name
        person.last_name = surename
        person.save()
        return redirect('/persons/')


def movie_edit(request, id):
    movie = Movie.objects.get(id=id)
    person = Person.objects.all()
    if request.method == "GET":
        return render(request, 'movie_edit.html', {'movie': movie, 'person': person})
    if request.method == "POST":
        title = request.POST.get("title")
        year = request.POST.get("year")
        rating = request.POST.get("rating")
        director_id = request.POST.get("director_id")
        screenplay_id = request.POST.get("screenplay_id")
        movie.title = title
        movie.year = year
        movie.rating = rating
        movie.director_id = director_id
        movie.screenplay_id = screenplay_id
        movie.save()
        return redirect('/movies/')


def add_person(request):
    person = Person()
    if request.method == "GET":
        return render(request, 'add_person.html', {'person': person})
    if request.method == "POST":
        name = request.POST['first_name']
        surename = request.POST.get("last_name")
        person.first_name = name
        person.last_name = surename
        person.save()
        return redirect('/persons/')


def add_movie(request):
    movie = Movie()
    person = Person.objects.all()
    if request.method == "GET":
        return render(request, 'add_movie.html', {'movie': movie, 'person': person})
    if request.method == "POST":
        title = request.POST.get("title")
        year = request.POST.get("year")
        rating = request.POST.get("rating")
        director_id = request.POST.get("director_id")
        screenplay_id = request.POST.get("screenplay_id")
        movie.title = title
        movie.year = year
        movie.rating = rating
        movie.director_id = director_id
        movie.screenplay_id = screenplay_id
        movie.save()
        return redirect('/movies/')

def search_movie(request):
    if request.method == "GET":
        return render(request, 'search_movie.html')
    if request.method == "POST":
        title = request.POST.get('title')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        year_from = request.POST.get('year_from')
        year_to = request.POST.get('year_to')
        rating_from = request.POST.get('rating_from')
        rating_to = request.POST.get('rating_to')
        genre = request.POST.get('genre').split(',')
        if title:
            movies = Movie.objects.filter(title=title)
        else:
            movies = Movie.objects.all()
        if year_from:
            movies = movies.filter(year__gte=year_from)
        if year_to:
            movies = movies.filter(year__lte=year_to)
        if rating_from:
            movies = movies.filter(rating__gte=rating_from)
        if rating_to:
            movies = movies.filter(rating__lte=rating_to)
        if genre:
            pass #to do
        if first_name:
            pass #to do
        if last_name:
            pass #to do

        return render(request, 'search_movie.html', {
            'movies': movies })