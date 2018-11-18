from django.conf import settings

from accounts import models as account_models

User = settings.AUTH_USER_MODEL

from rest_framework import serializers
from rest_framework.authtoken.models import Token

class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta:
        model = User

        fields = (
            'auth_token', 'username', 'is_active'
        )

    def get_auth_token(self, obj):
        token, _ = Token.objects.get_or_create(user=obj)
        return token.key

