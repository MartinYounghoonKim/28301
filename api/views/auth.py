"""
유저 인증 및 생성 관련 View
"""

from rest_framework import authentication, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from ..serializers import UserSerializer
from ..models import User


class UserAuthentication(APIView):
    """
    유저 인증 클래스
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """
        회원 정보를 반환합니다.
        """

        user_data = [
            {
                "ID": user.userId,
                "Nickname": user.userName,
                "Password": user.password,
                "Duty": user.duty,
            }
            for user in User.objects.all()
        ]
        return Response(user_data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        회원 정보를 추가합니다.
        """
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(data=None, status=status.HTTP_400_BAD_REQUEST)
