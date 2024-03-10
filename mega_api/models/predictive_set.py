"""Module for Predictive Set Model"""
from django.db import models
from .ball import Ball
from .mega_ball import MegaBall


class PredictiveSet(models.Model):
    """Predictive Set Model"""

    date = models.DateField(auto_now=False, auto_now_add=False)
    first_ball = models.ForeignKey(
        Ball, on_delete=models.RESTRICT, related_name="First Number+")
    second_ball = models.ForeignKey(
        Ball, on_delete=models.RESTRICT, related_name="Second Ball+")
    third_ball = models.ForeignKey(
        Ball, on_delete=models.RESTRICT, related_name="Third Ball+")
    fourth_ball = models.ForeignKey(
        Ball, on_delete=models.RESTRICT, related_name="Fourth Ball+")
    fifth_ball = models.ForeignKey(
        Ball, on_delete=models.RESTRICT, related_name="Fifth Ball+")
    mega_ball = models.ForeignKey(
        MegaBall, on_delete=models.RESTRICT, related_name="Mega Ball+")
