import graphene
from movies.api.models import Movie
from .type import MovieType


class MovieCreateMutation(graphene.Mutation):
    class Arguments:
        title=graphene.String(required=True)
        year=graphene.Int(required=True)
    movie=graphene.Field(MovieType)
    def mutate(self,info,title,year):
        movie=Movie.objects.create(title=title,year=year)
        return MovieCreateMutation(movie=movie)

class MovieUpdateMutation(graphene.Mutation):
    class Arguments:
        title=graphene.String()
        year=graphene.Int()
        id=graphene.ID(required=True)
    movie=graphene.Field(MovieType)

    def mutate(self,info,**kwargs):
        id=kwargs.get('id')
        title = kwargs.get('title')
        year = kwargs.get('year')
        movie = Movie.objects.get(pk=id)
        if title is not None:
            movie.title=title
        if year is not None:
            movie.year=year
        movie.save()
        return MovieUpdateMutation(movie=movie)

class MovieDeleteMutation(graphene.Mutation):
    class Arguments:
        id=graphene.ID(required=True)
    movie=graphene.Field(MovieType)

    def mutate(self,info,id):
        movie=Movie.objects.get(pk=id)
        movie.delete()
        return MovieDeleteMutation(movie=None)