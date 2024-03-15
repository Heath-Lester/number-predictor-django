from rest_framework.serializers import ModelSerializer
from mega_api.models.winning_set import WinningSet
from mega_api.serializers import BallSerializer, MegaBallSerializer


class WinningSetSerializer(ModelSerializer):
    """JSON serializer for Winning Sets"""
    first_ball = BallSerializer()
    second_ball = BallSerializer()
    third_ball = BallSerializer()
    fourth_ball = BallSerializer()
    fifth_ball = BallSerializer()
    mega_ball = MegaBallSerializer()

    class Meta:
        """Winning Set Meta"""
        model: type = WinningSet
        fields: tuple[str] = (
            'id',
            'date',
            'first_ball',
            'second_ball',
            'third_ball',
            'fourth_ball',
            'fifth_ball',
            'mega_ball',
            'megaplier',
            'jackpot_winners',
            'five_match_winners',
            'four_match_w_mega_winners',
            'four_match_winners',
            'three_match_w_mega_winners',
            'three_match_winners',
            'two_match_w_mega_winners',
            'one_match_w_mega_winners',
            'mega_match_winners',
            'estimated_jackpot',
            'cash_option',
            'five_match_prize',
            'four_match_w_mega_prize',
            'four_match_prize',
            'three_match_w_mega_prize',
            'three_match_prize',
            'two_match_w_mega_prize',
            'one_match_w_mega_prize',
            'mega_match_prize',
            'jackpot_megaplier_winners',
            'five_match_megaplier_winners',
            'four_match_w_mega_megaplier_winners',
            'four_match_megaplier_winners',
            'three_match_w_mega_megaplier_winners',
            'three_match_megaplier_winners',
            'two_match_w_mega_megaplier_winners',
            'one_match_w_mega_megaplier_winners',
            'mega_match_megaplier_winners',
            'five_match_megaplier_prize',
            'four_match_w_mega_megaplier_prize',
            'four_match_megaplier_prize',
            'three_match_w_mega_megaplier_prize',
            'three_match_megaplier_prize',
            'two_match_w_mega_megaplier_prize',
            'one_match_w_mega_megaplier_prize',
            'mega_match_megaplier_prize'
        )
        depth: int = 1
