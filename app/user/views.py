"""
Views for the User API
"""
from rest_framework import generics

from user.serializers import UserSerializers

class CreateUserview(generics.CreateAPIView):
    """create a new user in the system"""
    serializer_class = UserSerializers
