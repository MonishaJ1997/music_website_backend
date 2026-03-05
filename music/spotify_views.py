from django.http import JsonResponse
from django.conf import settings
import base64
import requests

SPOTIFY_CLIENT_ID = settings.SPOTIFY_CLIENT_ID
SPOTIFY_CLIENT_SECRET = settings.SPOTIFY_CLIENT_SECRET

def spotify_token(request):
    # Encode client ID & secret for Basic Auth
    auth_header = base64.b64encode(f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}".encode()).decode()
    token_url = "https://accounts.spotify.com/api/token"
    response = requests.post(
        token_url,
        headers={"Authorization": f"Basic {auth_header}"},
        data={"grant_type": "client_credentials"}
    )
    data = response.json()
    return JsonResponse(data)