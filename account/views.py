from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializers import LoginSerializer, UserSerializer


class LoginView(APIView):
    permission_classes = [~IsAuthenticated]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            raise ValidationError('Login yoki parol noto\'g\'ri')

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key
        })


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        serializer = UserSerializer(user)

        return Response(serializer.data)
