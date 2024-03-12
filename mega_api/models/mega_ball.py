"""Module for Mega Ball Model"""
from django.db.models import Model, PositiveSmallIntegerField


class MegaBall(Model):
    """Mega Ball Model"""
    number = PositiveSmallIntegerField()
