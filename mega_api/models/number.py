"""Module for Number Model"""
from django.db import models

class Number(models.Model):
    """Number Model"""

    number = models.PositiveSmallIntegerField()
