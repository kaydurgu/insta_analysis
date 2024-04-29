from django.db import models


class InstagramUser(models.Model):
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class InstagramUserProfile(models.Model):

    user = models.ForeignKey(InstagramUser, on_delete=models.CASCADE)
    datatime = models.DateTimeField(auto_created=True)
    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)
    followers_list = models.TextField(blank=True)
    following_list = models.TextField(blank=True)

class InstagramUserPosts(models.Model):

    user = models.ForeignKey(InstagramUser, on_delete=models.CASCADE)
    posts_count = models.IntegerField(default=0)
    posts_list = models.TextField(blank=True)
    most_liked_post = models.CharField(max_length=255, blank=True)
    most_commented_post = models.CharField(max_length=255, blank=True)

class InstagramPostFriends(models.Model):

    user = models.ForeignKey(InstagramUser, on_delete=models.CASCADE)
    user_following_but_not_followed_list = models.TextField(blank=True)
    user_followed_but_not_following_list = models.TextField(blank=True)
    mutual_lıst = models.TextField(blank=True)
    follower_who_liked_the_most_posts = models.CharField(max_length=255, blank=True)
    follower_who_commented_the_most_post = models.CharField(max_length=255, blank=True)
