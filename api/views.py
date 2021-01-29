from api.models import Client, License, Project
from api.serializers import (
    ClientSerializer,
    LicenseSerializer,
    ProjectSerializer,
    MessageSerializer,
)
from rest_framework import generics

# Create your views here.
class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ClientList(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class LicenseList(generics.ListAPIView):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer


class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
