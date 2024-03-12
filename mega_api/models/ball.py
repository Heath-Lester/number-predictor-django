"""Module for Ball Model"""
from django.db.models import Model, PositiveSmallIntegerField


class Ball(Model):
    """Ball Model"""
    number = PositiveSmallIntegerField()
