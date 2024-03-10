"""Module for Winning Set Model"""
from django.db import models
from .ball import Ball
from .power_ball import PowerBall


class WinningSet(models.Model):
    """Winning Set Model"""

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
        PowerBall, on_delete=models.RESTRICT, related_name="Mega Ball+")
    megaplier = models.PositiveSmallIntegerField()
    estimated_jackpot = models.PositiveBigIntegerField()
    cash_option = models.PositiveBigIntegerField()
    five_match_prize = models.PositiveIntegerField()
    four_w_mega_match_prize = models.PositiveIntegerField()
    four_match_prize = models.PositiveIntegerField()
    three_w_mega_match_prize = models.PositiveIntegerField()
    three_match_prize = models.PositiveIntegerField()
    two_w_mega_match_prize = models.PositiveIntegerField()
    one_w_mega_match_prize = models.PositiveIntegerField()
    mega_match_prize = models.PositiveIntegerField()
    jackpot_winners = models.PositiveIntegerField()
    five_matches = models.PositiveIntegerField()
    four_w_mega_matches = models.PositiveIntegerField()
    four_matches = models.PositiveIntegerField()
    three_w_mega_matches = models.PositiveIntegerField()
    three_matches = models.PositiveIntegerField()
    two_w_mega_matches = models.PositiveIntegerField()
    one_w_mega_matches = models.PositiveIntegerField()
    mega_matches = models.PositiveIntegerField()
