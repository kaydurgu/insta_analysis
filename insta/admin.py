from django.contrib import admin
from .models import InstagramUser,InstagramUserProfile,InstagramUserPosts,InstagramUserFriends
# Register your models here.

admin.site.register(InstagramUser)
admin.site.register(InstagramUserProfile)
admin.site.register(InstagramUserPosts)
admin.site.register(InstagramUserFriends)