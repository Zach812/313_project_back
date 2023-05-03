from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Movie, Rating, Character
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','groups']
    
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url','name']
        
class MovieSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(source='pk',read_only=True)
    class Meta:
        model = Movie
        fields = ['id','name','description','picture','order']
        
class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ['movieId','name','profile']
        
class RatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rating
        fields = ['movieId','rating','comment','name']
        
