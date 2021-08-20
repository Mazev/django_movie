from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, DetailView

from django_movie.movies.forms import ReviewForm
from django_movie.movies.models import Movie


class MoviesView(ListView):
    #   Списък на филмите

    movies = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    #  Пълно описание на филмите

    model = Movie
    slug_field = 'url'


class AddReview(View):
    # Коментари към филма

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()

        return redirect(movie.absolute_url())
