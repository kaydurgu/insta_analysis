from rest_framework import serializers
from .models import InstagramUser, InstagramUserProfile, InstagramUserPosts, InstagramUserFriends

class InstagramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramUser
        fields = ['id', 'username']
class InstagramUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramUserProfile
class InstagramUserPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramUserPosts
class InstagramUserFriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramUserFriends