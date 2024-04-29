from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import InstagramUserSerializer
from .models import InstagramUser
import requests
import config
class InstagramChecker(generics.ListCreateAPIView):
    queryset = InstagramUser.objects.all()
    serializer_class = InstagramUserSerializer
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        serializer = InstagramUserSerializer(data={'username': username})
        if serializer.is_valid():
            serializer.save()
        #############   followers
            url = config.url_followers
            querystring = {"username_or_id_or_url": username}
            headers = {
                config.x_key: config.API_KEY,
                config.x_host: config.API_X
            }
            response = requests.get(url, headers=headers, params=querystring)
            followers_count = response.json()['data']['total']
            followers_lst = []
            for item in response.json()['data']['items']:
                followers_lst.append(item['username'])
        #############  followings
            url = config.url_followings
            querystring = {"username_or_id_or_url": username}
            headers = {
                config.x_key: config.API_KEY,
                config.x_host: config.API_X
            }
            response = requests.get(url, headers=headers, params=querystring)
            followings_count = response.json()['data']['total']
            followings_lst = []
            for item in response.json()['data']['items']:
                followings_lst.append(item['username'])
            print(followers_count, followers_lst, followings_count, followings_lst)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class InstagramCheckUser(APIView):
    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')
        existing_user = InstagramUser.objects.filter(username=username).exists()
        if existing_user:




            pass
        else:
            return Response({'message': 'Username does not exists in our db make sure to go '}, status=status.HTTP_400_BAD_REQUEST)
class InstagramGetFollowers(APIView):
    pass

class InstagramGetFollowings(APIView):
    pass
class AllCheckedUsers(APIView):
    def get(self, request, *args, **kwargs):
        queryset = InstagramUser.objects.all()
        serializer = InstagramUserSerializer(queryset, many=True)
        return Response(serializer.data)