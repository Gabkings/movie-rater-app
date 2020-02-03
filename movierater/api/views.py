from rest_framework import viewsets
from .serializers import MovieSerializer, RatingSerializer
from .models import Movie, Rating
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:
            movie = Movie.objects.get(id=pk)
            user = User.objects.get(id=1)
            stars = request.data['stars']

            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                responce = {'message': 'Ratings updated', "data":serializer.data}
                return Response(responce,  status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(user=user, movie=movie, stars=stars)
                serializer = RatingSerializer(rating, many=False)

                responce = {'message': 'Ratings created', 'data': serializer.data}

                return Response(responce, status=status.HTTP_200_OK)

        else:
            responce = {'message':'Stars is required'}

            return Response(responce, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer




