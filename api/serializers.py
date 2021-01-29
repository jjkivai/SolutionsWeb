from api.models import Client, License, Message, Project, ProjectImage
from rest_framework.serializers import ModelSerializer, StringRelatedField


class ProjectImageSerializer(ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = "__all__"


class ProjectSerializer(ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = "__all__"


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class LicenseSerializer(ModelSerializer):
    class Meta:
        model = License
        fields = "__all__"


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
