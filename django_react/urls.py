from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('movies', views.MoviesViewSet, 'movie')

urlpatterns = [
    path('', views.home, name="home"),
]

urlpatterns += router.urls
