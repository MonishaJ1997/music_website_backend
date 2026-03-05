# music/serializers.py
from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    film_image = serializers.ImageField(source="film.image", read_only=True)
    film_name = serializers.CharField(source="film.name", read_only=True)
    film_section = serializers.IntegerField(source="film.section.id", read_only=True)

    class Meta:
        model = Song
        fields = [
            "id",
            "title",
            "spotify_uri",
            "fans",
            "film",
            "film_name",
            "film_image",
            "film_section",
        ]
from rest_framework import serializers
from .models import Film

class FilmSerializer(serializers.ModelSerializer):
    section_id = serializers.IntegerField(source="section.id")

    class Meta:
        model = Film
        fields = ["id", "name", "image", "section_id"]

        # serializers.py
from rest_framework import serializers
from .models import AuthBanner

class AuthBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthBanner
        fields = '__all__'

        from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

# REGISTER
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password','name']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


# LOGIN
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(
            username=data['email'],  # important
            password=data['password']
        )
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        return user