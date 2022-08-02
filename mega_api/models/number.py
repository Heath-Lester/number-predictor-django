"""Module for Number Model"""
from django.db import models
from mega_api.models import Winning_Set

class Number(models.Model):
    """Number Model"""
    number = models.PositiveSmallIntegerField()
    position = models.PositiveSmallIntegerField()
    winning_set = models.ForeignKey(Winning_Set, on_delete=models.RESTRICT, related_name="Winning Set+")
