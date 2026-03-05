from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Song
from .serializers import SongSerializer   # ⚠ change this

@api_view(['GET'])
def get_all_songs(request):
    songs = Song.objects.all().order_by('-id')
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_album_songs(request, film_id):   # rename album_id → film_id
    songs = Song.objects.filter(film_id=film_id)
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_single_song(request, song_id):
    try:
        song = Song.objects.get(id=song_id)
        serializer = SongSerializer(song)
        return Response(serializer.data)
    except Song.DoesNotExist:
        return Response({"error": "Song not found"}, status=404)

from rest_framework import generics
from .models import Film
from .serializers import FilmSerializer

class FilmListView(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def get_serializer_context(self):
        return {"request": self.request}


from rest_framework.generics import ListAPIView
from .models import AuthBanner
from .serializers import AuthBannerSerializer

class AuthBannerListView(ListAPIView):
    queryset = AuthBanner.objects.all().order_by('-created_at')
    serializer_class = AuthBannerSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer
class RegisterView(APIView):
    def post(self, request):
        try:
            serializer = RegisterSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({"message": "User created"})

            return Response(serializer.errors, status=400)

        except Exception as e:
            print("ERROR:", str(e))  # 👈 see terminal
            return Response({"error": str(e)}, status=500)

# LOGIN
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response(
                {"error": "Email and password required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 🔥 IMPORTANT: use username=email
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return Response({
                "message": "Login successful",
                "name": user.name,
                "email": user.email
            })

        return Response(
            {"error": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )
class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logged out"})
#
class CheckAuthView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return Response({
                "authenticated": True,
                "name": request.user.name
            })
        return Response({"authenticated": False})
    

    
from rest_framework.generics import ListAPIView




from rest_framework.filters import SearchFilter
from .models import Song
from .serializers import SongSerializer

class SongSearchView(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = [SearchFilter]
    search_fields = [
        "title",          # song title
        "film__name",     # film name
    ]