from django.shortcuts import render
from rest_framework import viewsets
from .models import Land
from .serializers import LandSerializer
from rest_framework.permissions import IsAuthenticated


class LandViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Land.objects.all()
    serializer_class = LandSerializer
