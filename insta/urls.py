
from django.urls import path
from .views import InstagramChecker, AllCheckedUsers, InstagramCheckUser, InstagramGetFollowers, InstagramGetFollowings, InstagramGetMostCommentedPost, InstagramGetMostLikedPost,InstagramUserGetNotFollowingBack, InstagramUserGetNotFollowedBack, InstagramUserGetMutualFollowing, InstagramCheckUserPost
urlpatterns = [
    path('check/', InstagramChecker.as_view()),
    path('check/<str:user>/info', InstagramCheckUser.as_view()),
    path('check/<str:user>/posts', InstagramCheckUserPost.as_view()),
    path('check/<str:user>/followers', InstagramGetFollowers.as_view()),
    path('check/<str:user>/following', InstagramGetFollowings.as_view()),
    path('check/<str:user>/most_liked_post', InstagramGetMostLikedPost.as_view()),
    path('check/<str:user>/most_commented_post', InstagramGetMostCommentedPost.as_view()),
    path('check/<str:user>/not_followed_back', InstagramUserGetNotFollowedBack.as_view()),
    path('check/<str:user>/not_following_back',InstagramUserGetNotFollowingBack.as_view()),
    path('check/<str:user>/mutual_following', InstagramUserGetMutualFollowing.as_view()),
    path('all_checked_users/', AllCheckedUsers.as_view()),
]
