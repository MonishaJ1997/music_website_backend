from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name or "Unnamed Section"
class Film(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="films/")

    def __str__(self):
        return self.name

class Song(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name="songs")
    title = models.CharField(max_length=200)
    spotify_uri = models.CharField(max_length=100, blank=True, null=True)
    audio = models.FileField(upload_to="audio/", null=True, blank=True)
    fans = models.CharField(max_length=20, default="2.9k")

    def __str__(self):
        return self.title

    

        # models.py
from django.db import models

class AuthBanner(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='auth_banner/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()   # ✅ VERY IMPORTANT

    def __str__(self):
        return self.email