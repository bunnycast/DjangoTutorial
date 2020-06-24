from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics

from quickstart.serializers import UserSerializer, GroupSerializer

# # Using ModelViewSet
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

# # Using generic
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = GroupSerializer


# Using ViewSet
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer