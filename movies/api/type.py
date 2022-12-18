import graphene
from graphene_django.types import DjangoObjectType
from .models import Movie,Director

class MovieType(DjangoObjectType):
    class Meta:
        model=Movie

    movie_age=graphene.String()

    def resolve_movie_age(self, info):
        return "Old movie" if self.year < 2000 else "New movie"


class DirectorType(DjangoObjectType):
     class Meta:
         model=Director