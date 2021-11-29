import base64
"""View for Winning Drawings"""
from django.views.generic.base import View
from rest_framework import status
from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.http import HttpResponseServerError
from django.core.files.base import ContentFile
from django.contrib.auth.models import User

class Winning_Drawings(View):
    
    def list(self, request):
        """Handles GET requests for all Winning Drawings"""
        
        