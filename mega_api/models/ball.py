"""Module for Ball Model"""
from django.db import models


class Ball(models.Model):
    """Ball Model"""
    number = models.PositiveSmallIntegerField()
