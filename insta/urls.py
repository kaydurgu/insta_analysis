
from django.urls import path
from .views import InstagramChecker, AllCheckedUsers, InstagramCheckUser
urlpatterns = [
    path('check/', InstagramChecker.as_view(), name='instagram-checker'),
    path('check/<str:user>', InstagramCheckUser.as_view(), name='instagram-checker'),
    path('all_checked_users/', AllCheckedUsers.as_view(), name='instagram-checker'),
]
