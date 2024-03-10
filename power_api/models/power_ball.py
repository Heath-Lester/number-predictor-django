"""Module for Power Ball Model"""
from django.db import models


class PowerBall(models.Model):
    """Power Ball Model"""
    number = models.PositiveSmallIntegerField()
