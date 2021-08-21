from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, DetailView

from django_movie.movies.forms import ReviewForm
from django_movie.movies.models import Movie, Category, Genre


class GenreYear:
    # жанрове и години
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values('year')


class AddReview(View):
    """Коментари към филма"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


class MoviesView(ListView, GenreYear):
    #   Списък на филмите

    movies = Movie
    queryset = Movie.objects.filter(draft=False)




class MovieDetailView(DetailView):
    #  Пълно описание на филмите

    model = Movie
    slug_field = 'url'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context


class FilterMoviesView(GenreYear, ListView):
    # Филтър филми
    def get_queryset(self):
        queryset = Movie.objects.filter(year__in=self.request.GET.getlist('year'))

        return queryset


class Search(ListView):
    # Търсачка за филми
    paginate_by = 3

    def get_queryset(self):
        return Movie.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context