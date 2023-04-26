from django.shortcuts import render
from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer, RatingSerializer,MovieSerializer,CharacterSerializer
from .models import Movie,Rating,Character
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer    

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Movies to be viewed or edited
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    def get_paginated_response(self, data):
        return Response(data)
    
class RatingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Ratings to be viewed or edited
    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    def get_paginated_response(self, data):
        return Response(data)
    
class CharacterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Chracters to be viewed or edited
    """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    def get_paginated_response(self, data):
        return Response(data)