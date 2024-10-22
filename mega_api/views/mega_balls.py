from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response
from mega_api.models import MegaBall
from mega_api.serializers import MegaBallSerializer
from django.http import HttpResponseServerError, HttpResponseNotAllowed, HttpResponseNotFound


class MegaBalls(ViewSet):
    """Class containing CRUD operations for Mega Balls"""

    def list(self, request) -> Response:
        """Handles GET requests for all Mega Balls"""

        try:
            mega_balls: list[MegaBall] = MegaBall.objects.all()

            serializer = MegaBallSerializer(
                mega_balls, many=True, context={'request': request})

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as exception:
            return HttpResponseServerError(exception)

    def destroy(self, request, pk=None) -> Response:
        """Handles DELETE requests for all Mega Balls"""
        return HttpResponseNotAllowed(permitted_methods=['GET'])

    def create(self, request) -> Response:
        """Handles POST requests for all Mega Balls"""
        return HttpResponseNotAllowed(permitted_methods=['GET'])

    def update(self, request, pk=None) -> Response:
        """Handles POST requests for all Mega Balls"""
        return HttpResponseNotAllowed(permitted_methods=['GET'])

    def partial_update(self, request, pk=None) -> Response:
        """Handles PATCH requests for all Balls"""
        return HttpResponseNotAllowed(permitted_methods=['GET'])

    def retrieve(self, request, pk=None) -> Response:
        """Handles GET requests for a single Mega Ball"""

        try:
            mega_ball: MegaBall = MegaBall.objects.get(pk=pk)

            serializer = MegaBallSerializer(
                mega_ball, context={'request': request})

            return Response(serializer.data, status=status.HTTP_200_OK)

        except MegaBall.DoesNotExist as exception:
            return HttpResponseNotFound({'message': exception.args[0]})

        except Exception as exception:
            return HttpResponseServerError(exception)
