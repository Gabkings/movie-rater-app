from rest_framework import serializers

from .models import  Movie, Rating
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title','description',)
    @action(detail=True, methods=['POST'])
    def rate_movie(self,request, pk=None):
        responce = {'message': 'It is working'}

        return Response(responce, status=status.HTTP_200_OK)

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id','user','movie','stars')

