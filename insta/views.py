from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import InstagramUserSerializer
from .models import InstagramUser, InstagramUserProfile, InstagramUserPosts, InstagramUserFriends
import requests
import config
from django.utils import timezone
class InstagramChecker(generics.ListCreateAPIView):
    queryset = InstagramUser.objects.all()
    serializer_class = InstagramUserSerializer
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        try:
            user_obj = InstagramUser.objects.get(username=username)
            user_obj.delete()
        except:
            pass
        try:
            user_obj = InstagramUserProfile.objects.get(user=username)
            user_obj.delete()
        except:
            pass
        try:
            user_obj = InstagramUserFriends.objects.get(user=username)
            user_obj.delete()
        except:
            pass
        try:
            user_obj = InstagramUserPosts.objects.get(user=username)
            user_obj.delete()
        except:
            pass
        serializer = InstagramUserSerializer(data={'username': username})
        if serializer.is_valid():
            ######################### info
            url = config.url_info
            querystring = {"username_or_id_or_url": username}
            headers = {
                config.x_key: config.API_KEY,
                config.x_host: config.API_X
            }
            response = requests.get(url, headers=headers, params=querystring)
            is_private = response.json()['data']['is_private']

            if is_private:
                return Response({'error: sorry account is private'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            country = None
            bio = response.json()['data']['biography']
            full_name = response.json()['data']['full_name']
            is_private = response.json()['data']['is_private']
            profile_pic = response.json()['data']['profile_pic_url']
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


        ##################### posts
            url = config.url_posts
            querystring = {"username_or_id_or_url": username}
            headers = {
                config.x_key: config.API_KEY,
                config.x_host: config.API_X
            }
            response = requests.get(url, headers=headers, params=querystring)
            post_count = response.json()['data']['count']
            max_comments = 0
            max_commented_post_code = ''
            max_likes = 0
            max_liked_post_code = ''
            for post in response.json()['data']['items']:
                if max_likes < post['like_count']:
                    max_likes = post['like_count']
                    max_liked_post_code = post['code']
                if max_comments < post['comment_count']:
                    max_comments = post['comment_count']
                    max_commented_post_code = post['code']
            print(InstagramUser.objects.get_queryset())
            instagram_user_profile = InstagramUserProfile.objects.create(
                user=username,
                profile_pic_link=profile_pic,
                country="",
                biography=bio,
                datatime=timezone.now(),
                full_name=full_name,
                is_private=is_private,
                followers_count=followers_count,
                following_count=followings_count,
                followers_list=followers_lst,
                following_list=followings_lst
            )
            instagram_user_post = InstagramUserPosts.objects.create(
                user=username,
                posts_count=post_count,
                most_liked_post='https://www.instagram.com/p/{max_liked_post_code}/',
                most_commented_post='https://www.instagram.com/p/{max_commented_post_code}/',
            )
            instagram_user_profile.save()
            instagram_user_post.save()

            not_followed_back = [user for user in followings_lst if user not in followers_lst]
            not_following_back = [user for user in followers_lst if user not in followings_lst]
            mutual_following = [user for user in followers_lst if user in followings_lst]

            instagram_user_friends = InstagramUserFriends.objects.create(
                user=username,
                not_followed_back=not_followed_back,
                not_following_back=not_following_back,
                mutual_list=mutual_following,
            )
            instagram_user_friends.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InstagramCheckUser(APIView):
    def get(self, request, user):
        try:
            user_obj = InstagramUser.objects.get(username=user)
            return Response({'followers': 'vrode vse zaebis'}, status=status.HTTP_200_OK)
        except InstagramUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
class InstagramGetFollowers(APIView):
    def get(self, request, user):
        try:
            user_obj = InstagramUser.objects.get(username=user)
            return Response({'followers': 'vrode vse zaebis'}, status=status.HTTP_200_OK)
        except InstagramUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

class InstagramGetFollowings(APIView):
    pass
class AllCheckedUsers(APIView):
    def get(self, request, *args, **kwargs):
        queryset = InstagramUser.objects.all()
        serializer = InstagramUserSerializer(queryset, many=True)
        return Response(serializer.data)