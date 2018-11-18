from django.contrib.auth import authenticate
from django.conf import settings
from rest_framework import generics, permissions, response, status, filters
from rest_framework.views import APIView

from . import serializers as account_serializer
from . import models as account_model
import django_filters
User = settings.AUTH_USER_MODEL


from django.contrib.auth import login, logout

class LoginView(APIView):
    """Login of a user
    """

    error_messages = {
        'inactive_account': "Account is Not Active",
        'invalid_username': "wrong Username or password",
    }

    permission_classes = (permissions.AllowAny,)

    AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.AllowAllUsersModelBackend']

    def post(self, request, format=None):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)

        try:
            user = User.objects.get(user_id=username)
            if not user.is_active:
                raise serializers.ValidationError(
                    self.error_messages['inactive_account']
                )

        except User.DoesNotExist:
            raise serializers.ValidationError(
                self.error_messages['invalid_username']
            )

        user = authenticate(username=username, password=password)
        if user is not None:

            token_serializer = account_serializer.TokenSerializer(
                                        instance=user
                                )

            data = token_serializer.data

            return Response(
                data=data,
                status=status.HTTP_200_OK
                )
        else:
            raise serializers.ValidationError(
                self.error_messages['invalid_username'])

class LogoutView(APIView):
    """ log out the user
    """

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        """ post method for the logout the user """
        Token.objects.filter(user=request.user).delete()
        return response.Response({'msg': "user logout successfully."}, status=status.HTTP_200_OK)


class ChangePassword(APIView):
    def get(self, request, format=None):
        user_id = request.GET.get('user', '')
        password = request.GET.get('password', '')
        _response = {
                    'msg' : '',
                    'is_success' : False,
                    'user_details' : {}
                    }
        if user_id:
            user = User.objects.get(user_id=user_id)
            if not password:
                password = "new_password"
            user.set_password(password)
            user.save()
            #Token.objects.filter(user__advisor_id=user_id).delete()

            _response['is_success'] = True
            _response['user_details'] = {
                'username' : user.user_id,
                'is_active': user.is_active,
                'password': password
                }
            Token.objects.filter(user=user).delete()
            return Response(_response)

        _response['msg'] = 'User id is not present'
        return Response(_response, status=status.HTTP_400_BAD_REQUEST)





