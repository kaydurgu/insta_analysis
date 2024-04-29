from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import InstagramUserSerializer
from .models import InstagramUser
class InstagramChecker(APIView):
    def post(self, request):
        serializer = InstagramUserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            return Response({'message': 'Checking followers...'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InstagramCheckUser(APIView):
    def get(self, request, *args, **kwargs):
        username = kwargs.get('user')
        try:
            user_exists = InstagramUser.objects.filter(username=username).exists()
            if user_exists:
                return Response({'message': f'User {username} exists'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': f'User {username} does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AllCheckedUsers(APIView):
    def get(self, request, *args, **kwargs):
        queryset = InstagramUser.objects.all()
        serializer = InstagramUserSerializer(queryset, many=True)
        return Response(serializer.data)