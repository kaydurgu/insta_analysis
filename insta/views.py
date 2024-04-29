from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import InstagramUserSerializer
from .models import InstagramUser
from instabot import Bot
import requests
import config
import os
import glob
class InstagramChecker(APIView):
    pass
class InstagramCheckUser(APIView):

   pass

class InstagramGetFollowers(APIView):
    def get(self, request, *args, **kwargs):
        username = kwargs.get('user')
        url = "https://instagram-scraper-api2.p.rapidapi.com/v1/followers"
        querystring = {"username_or_id_or_url": username}
        headers = {
            "X-RapidAPI-Key": "e57077f1acmsh2b2d59c7b485939p194b13jsn90d518207444",
            "X-RapidAPI-Host": "instagram-scraper-api2.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        return JsonResponse({'followers': response.json()})

class InstagramGetFollowings(APIView):
    def get(self, request, *args, **kwargs):
        username = kwargs.get('user')
        url = "https://instagram-scraper-api2.p.rapidapi.com/v1/following"
        querystring = {"username_or_id_or_url": username}
        headers = {
            "X-RapidAPI-Key": "e57077f1acmsh2b2d59c7b485939p194b13jsn90d518207444",
            "X-RapidAPI-Host": "instagram-scraper-api2.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        return JsonResponse({'followings': response.json()})
class AllCheckedUsers(APIView):
    def get(self, request, *args, **kwargs):
        queryset = InstagramUser.objects.all()
        serializer = InstagramUserSerializer(queryset, many=True)
        return Response(serializer.data)