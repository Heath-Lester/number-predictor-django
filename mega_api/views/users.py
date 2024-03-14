from django.http import HttpResponseNotAllowed, HttpResponseServerError, HttpResponseNotFound
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from mega_api.serializers import UserSerializer


class Users(ViewSet):
    """Users for Mega
    Purpose: Allow a user to communicate with the Mega database to GET PUT POST and DELETE Users.
    Methods: GET PUT(id) POST
"""

    def retrieve(self, request, pk=None) -> Response:
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)

        except User.DoesNotExist as exception:
            return HttpResponseNotFound({'message': exception.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as exception:
            return HttpResponseServerError(exception, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request) -> Response:
        """Handle GET requests for all Users"""
        users = User.objects.all()
        serializer = UserSerializer(
            users, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None) -> Response:
        """Handles DELETE requests for all User"""
        return HttpResponseNotAllowed({'message': 'method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request) -> Response:
        """Handles POST requests for all Users"""
        return HttpResponseNotAllowed({'message': 'method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, pk=None) -> Response:
        """Handles POST requests for all Users"""
        return HttpResponseNotAllowed({'message': 'method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
