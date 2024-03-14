from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response
from mega_api.models import Ball
from mega_api.serializers import BallSerializer
from django.http import HttpResponseServerError, HttpResponseNotAllowed, HttpResponseNotFound


class Balls(ViewSet):
    """Class containing CRUD operations for Balls"""

    def list(self, request) -> Response:
        """Handles GET requests for all Balls"""

        try:
            balls: list[Ball] = Ball.objects.all()

            serializer = BallSerializer(
                balls, many=True, context={'request': request})

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as exception:
            return HttpResponseServerError(exception, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None) -> Response:
        """Handles DELETE requests for all Balls"""

        return HttpResponseNotAllowed({'message': 'method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request) -> Response:
        """Handles POST requests for all Balls"""

        return HttpResponseNotAllowed({'message': 'method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, pk=None) -> Response:
        """Handles POST requests for all Balls"""

        return HttpResponseNotAllowed({'message': 'method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request, pk=None) -> Response:
        """Handles GET requests for a single Ball"""

        try:
            ball: Ball = Ball.objects.get(pk=pk)

            serializer = BallSerializer(
                ball, context={'request': request})

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Ball.DoesNotExist as exception:
            return HttpResponseNotFound({'message': exception.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as exception:
            return HttpResponseServerError(exception, status=status.HTTP_500_INTERNAL_SERVER_ERROR)