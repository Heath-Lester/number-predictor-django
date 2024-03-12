from django.http import HttpResponseNotFound, HttpResponseServerError
from mega_api.models import Ball, MegaBall
from rest_framework import status


class BallUtils():

    @staticmethod
    def get_ball_by_number(number: str | int) -> Ball:
        try:
            number = int(number)
            referenced_ball = Ball.objects.get(number=number)
            return referenced_ball
        except Ball.DoesNotExist as ex:
            raise HttpResponseNotFound(
                {'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            raise HttpResponseServerError(
                ex, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def get_mega_ball_by_number(number: str | int) -> MegaBall:
        try:
            number = int(number)
            referenced_ball = MegaBall.objects.get(number=number)
            return referenced_ball
        except MegaBall.DoesNotExist as ex:
            raise HttpResponseNotFound(
                {'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            raise HttpResponseServerError(
                ex, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
