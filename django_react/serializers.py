from rest_framework.serializers import ModelSerializer
from .models import Movies


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movies
        fields = "__all__"
