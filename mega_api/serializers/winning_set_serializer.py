from rest_framework.serializers import ModelSerializer

from mega_api.models.winning_set import WinningSet
from mega_api.serializers.ball_serializer import BallSerializer
from mega_api.serializers.mega_ball_serializer import MegaBallSerializer


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
            'id', 'first_ball', 'second_ball', 'third_ball', 'fourth_ball', 'fifth_ball', 'mega_ball',
            'megaplier', 'estimated_jackpot', 'cash_option', 'five_match_prize', 'four_w_mega_match_prize', 'four_match_prize',
            'three_w_mega_match_prize', 'three_match_prize', 'two_w_mega_match_prize', 'one_w_mega_match_prize', 'mega_match_prize',
            'jackpot_winners', 'five_matches', 'four_w_mega_matches', 'four_matches', 'three_w_mega_matches', 'three_matches',
            'two_w_mega_matches', 'one_w_mega_matches', 'mega_matches',
        )
        depth: int = 1
