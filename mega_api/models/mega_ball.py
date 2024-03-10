"""Module for Mega Ball Model"""
from django.db import models


class MegaBall(models.Model):
    """Mega Ball Model"""
    number = models.PositiveSmallIntegerField()
