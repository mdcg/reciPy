from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.users_serializers import UserSerializer


class SignUpView(APIView):
    def post(self, request):
        user_to_register = UserSerializer(data=request.data)

        if user_to_register.is_valid():
            user = user_to_register.save()
            # When we save the 'User' model through the serializer,
            # Django does not call the password encryption method.
            # In order for the password to be encrypted, we need
            # to perform the method below.
            user.set_password(user.password)
            user.save()

            token = Token.objects.create(user=user)

            response_data = {
                'status': 'success',
                'data': {
                    'user': {
                        'id': user.id,
                        'token': token.key,
                    },
                },
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        response_data = {
            'status': 'fail',
            'data': user_to_register.errors,
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class SignInView(APIView):
    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        # Lol
        if not username or not password:
            response_data = {
                'status': 'fail',
                'data': {
                    'username': ['A username is required.'],
                    'password': ['A password is required.'],
                },
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)

            response_data = {
                'status': 'success',
                'data': {
                    'user': {
                        'id': user.id,
                        'token': token.key,
                    },
                },
            }
            return Response(response_data, status=status.HTTP_200_OK)

        response_data = {
            'status': 'fail',
            'data': None,
        }
        return Response(response_data, status=status.HTTP_403_FORBIDDEN)
