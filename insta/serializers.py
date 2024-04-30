from rest_framework import serializers
from .models import InstagramUser, InstagramUserProfile, InstagramUserPosts, InstagramUserFriends

class InstagramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramUser
        fields = ['id', 'username']
class InstagramUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramUserProfile
        fields = '__all__'
class InstagramUserPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramUserPosts
        fields = '__all__'
class InstagramUserMostLikedPost(serializers.ModelSerializer):
    class Meta:
        model = InstagramUserPosts
        fields = ['most_liked_post']
class InstagramUserMostCommentedPost(serializers.ModelSerializer):
    class Meta:
        model = InstagramUserPosts
        fields = ['most_commented_post']
class InstagramUserFriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramUserFriends
        fields = '__all__'
class InstagramUserNotFollowedBack(serializers.ModelSerializer):
    class Meta:
        model = InstagramUserFriends
        fields = ['not_followed_back']
class InstagramUserNotFollowingBack(serializers.ModelSerializer):
    class Meta:
        model = InstagramUserFriends
        fields = ['not_following_back']
class InstagramUserMutualFollowing(serializers.ModelSerializer):
    class Meta:
        model = InstagramUserFriends
        fields = ['mutual_list']
class InstagramUserFollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramUserProfile
        fields = ['followers_count', 'followers_list']

class InstagramUserFollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramUserProfile
        fields = ['following_count', 'following_list']
