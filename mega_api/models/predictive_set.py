"""Module for Predictive Set Model"""
from django.db.models import ForeignKey, Model, RESTRICT, DateField
from .ball import Ball
from .mega_ball import MegaBall


class PredictiveSet(Model):
    """Predictive Set Model"""

    created_date = DateField(auto_now=False, auto_now_add=False)
    prediction_date = DateField(auto_now=False, auto_now_add=False)
    first_ball = ForeignKey(
        Ball, on_delete=RESTRICT, related_name="First Number+")
    second_ball = ForeignKey(
        Ball, on_delete=RESTRICT, related_name="Second Ball+")
    third_ball = ForeignKey(
        Ball, on_delete=RESTRICT, related_name="Third Ball+")
    fourth_ball = ForeignKey(
        Ball, on_delete=RESTRICT, related_name="Fourth Ball+")
    fifth_ball = ForeignKey(
        Ball, on_delete=RESTRICT, related_name="Fifth Ball+")
    mega_ball = ForeignKey(
        MegaBall, on_delete=RESTRICT, related_name="Mega Ball+")
