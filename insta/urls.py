
from django.urls import path
from .views import InstagramChecker, AllCheckedUsers, InstagramCheckUser, InstagramGetFollowers, InstagramGetFollowings
urlpatterns = [
    path('check/', InstagramChecker.as_view()),
    path('check/<str:user>', InstagramCheckUser.as_view()),
    path('check/<str:user>/followers', InstagramGetFollowers.as_view()),
    path('check/<str:user>/following', InstagramGetFollowings.as_view()),
    path('all_checked_users/', AllCheckedUsers.as_view()),
]
