from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movies
from .serializers import MovieSerializer


# Create your views here.
def home(request):
    return HttpResponse("Home")


#
class MoviesViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Movies.objects.all()[:10]
    serializer_class = MovieSerializer

    @api_view(['GET'])
    def get_movies(self, request):
        return Response(MovieSerializer.data)


