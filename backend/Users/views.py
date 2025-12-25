from rest_framework import viewsets
from .models import UserProfile
from .serializers import SimpleUserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = SimpleUserSerializer

