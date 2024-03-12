"""Module for Winning Set Model"""
from django.db.models import ForeignKey, Model, RESTRICT, DateField, PositiveBigIntegerField, PositiveIntegerField, PositiveSmallIntegerField
from .ball import Ball
from .mega_ball import MegaBall


class WinningSet(Model):
    """Winning Set Model"""

    # Standard Data
    date = DateField(auto_now=False, auto_now_add=False)
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
    megaplier = PositiveSmallIntegerField()
    # Number of Standard Winners
    jackpot_winners = PositiveIntegerField(required=False)
    five_match_winners = PositiveIntegerField(required=False)
    four_match_w_mega_winners = PositiveIntegerField(required=False)
    four_match_winners = PositiveIntegerField(required=False)
    three_match_w_mega_winners = PositiveIntegerField(required=False)
    three_match_winners = PositiveIntegerField(required=False)
    two_match_w_mega_winners = PositiveIntegerField(required=False)
    one_match_w_mega_winners = PositiveIntegerField(required=False)
    mega_match_winners = PositiveIntegerField(required=False)
    # Standard Prizes
    estimated_jackpot = PositiveBigIntegerField(required=False)
    cash_option = PositiveBigIntegerField(required=False)
    five_match_prize = PositiveIntegerField(required=False)
    four_match_w_mega_prize = PositiveIntegerField(required=False)
    four_match_prize = PositiveIntegerField(required=False)
    three_match_w_mega_prize = PositiveIntegerField(required=False)
    three_match_prize = PositiveIntegerField(required=False)
    two_match_w_mega_prize = PositiveIntegerField(required=False)
    one_match_w_mega_prize = PositiveIntegerField(required=False)
    mega_match_prize = PositiveIntegerField(required=False)
    # Number of Megaplier Winners
    jackpot_megaplier_winners = PositiveIntegerField(required=False)
    five_match_megaplier_winners = PositiveIntegerField(required=False)
    four_match_w_mega_megaplier_winners = PositiveIntegerField(required=False)
    four_match_megaplier_winners = PositiveIntegerField(required=False)
    three_match_w_mega_megaplier_winners = PositiveIntegerField(required=False)
    three_match_megaplier_winners = PositiveIntegerField(required=False)
    two_match_w_mega_megaplier_winners = PositiveIntegerField(required=False)
    one_match_w_mega_megaplier_winners = PositiveIntegerField(required=False)
    mega_match_megaplier_winners = PositiveIntegerField(required=False)
    # Megaplier Prizes
    five_match_megaplier_prize = PositiveIntegerField(required=False)
    four_match_w_mega_megaplier_prize = PositiveIntegerField(required=False)
    four_match_megaplier_prize = PositiveIntegerField(required=False)
    three_match_w_mega_megaplier_prize = PositiveIntegerField(required=False)
    three_match_megaplier_prize = PositiveIntegerField(required=False)
    two_match_w_mega_megaplier_prize = PositiveIntegerField(required=False)
    one_match_w_mega_megaplier_prize = PositiveIntegerField(required=False)
    mega_match_megaplier_prize = PositiveIntegerField(required=False)

    # @property
    # def first_ball(self):
    #     return self.__first_ball

    # @first_ball.setter
    # def first_ball(self, value: Ball):
    #     self.first_ball: Ball = value

    # @property
    # def second_ball(self):
    #     return self.__second_ball

    # @second_ball.setter
    # def second_ball(self, value: Ball):
    #     self.second_ball = value

    # @property
    # def third_ball(self):
    #     return self.__third_ball

    # @third_ball.setter
    # def third_ball(self, value: Ball):
    #     self.third_ball = value

    # @property
    # def fourth_ball(self):
    #     return self.__fourth_ball

    # @fourth_ball.setter
    # def fourth_ball(self, value: Ball):
    #     self.fourth_ball = value

    # @property
    # def fifth_ball(self):
    #     return self.__fifth_ball

    # @fifth_ball.setter
    # def fifth_ball(self, value: Ball):
    #     self.fifth_ball = value

    # @property
    # def mega_ball(self):
    #     return self.__mega_ball

    # @mega_ball.setter
    # def mega_ball(self, value: MegaBall):
    #     self.mega_ball = value
