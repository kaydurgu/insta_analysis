from django.db import models


class InstagramUser(models.Model):
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class InstagramUserProfile(models.Model):

    user = models.CharField(max_length=255)
    profile_pic_link = models.CharField(max_length=255)
    country = models.CharField(max_length=255, default=None)
    biography = models.CharField(max_length=255, default=None)
    is_private = models.BooleanField(default=False)
    full_name = models.CharField(max_length=255, default=None)
    datatime = models.DateTimeField(auto_created=True)
    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)
    followers_list = models.TextField(blank=True)
    following_list = models.TextField(blank=True)

class InstagramUserPosts(models.Model):

    user = models.CharField(max_length=255)
    posts_count = models.IntegerField(default=0)
    most_liked_post = models.CharField(max_length=255, blank=True)
    most_commented_post = models.CharField(max_length=255, blank=True)

class InstagramUserFriends(models.Model):

    user = models.CharField(max_length=255)
    not_followed_back = models.TextField(blank=True)
    not_following_back = models.TextField(blank=True)
    mutual_list = models.TextField(blank=True)
