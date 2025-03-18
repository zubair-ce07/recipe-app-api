"""
Serializers for the user API view
"""
from django.contrib.auth import (
    get_user_model,
    authenticate
)

from django.utils.translation import gettext as _

from rest_framework import serializers

class UserSerializers(serializers.ModelSerializer):
    """Serializers for user object"""

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name', 'image', 'DOB', 'user_role', 'pka', 'ipi_number',
        'pro', 'label_affiliation', 'publisher_affiliation']
        extra_kwargs= {'password': {'write_only': True, 'min_length': 5}}

        def create(self, validate_data):
            """create and return a user with encrypted password"""
            return get_user_model().objects.create_user(**validate_data)

class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user Auth token"""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('requst'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs