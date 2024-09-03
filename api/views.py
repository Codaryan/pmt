from rest_framework import viewsets
from .models import Client, Project, ProjectUser
from .serializer import ClientSerializer, ProjectSerializer, ProjectUserSerializer

class ClientViewset(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    http_method_names = ['get','post','retrieve','put','patch','delete']

class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['get','post','retrieve','put','patch','delete']

class ProjectUserViewset(viewsets.ModelViewSet):
    queryset = ProjectUser.objects.all()
    serializer_class = ProjectUserSerializer
    http_method_names = ['get','post','retrieve','put','patch','delete']