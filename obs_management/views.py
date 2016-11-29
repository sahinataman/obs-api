from django.shortcuts import render
from rest_framework import viewsets 
from .models import Management
from .serializers import ManagementSerializer

class ManagementViewSet(viewsets.ModelViewSet):  
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer

