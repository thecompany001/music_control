from django.shortcuts import render
from .credentials import REDIRECT_URI, CLIENT_SECRET, CLIENT_ID
from rest_framework.views import APIView
from requests Request, post
from rest_framework import status
from rest_framework.response import Response

class AuthURL(APIView):
    def get(self, request, format=None):
        scopes = 'user-read-playback-state user-modify-playback-state user-read-currently-playing'

        url = Request('GET', 'https://accounts.spotify.com/authorize', params={
            'scope': scopes,
            'response_type': 'code',
            'redirect_uri': REDIRECT,
            'client_id': CLIENT_ID
        }).prepare.uri


        return Response({'url': url}, status=status.HTTP_200_OK)



