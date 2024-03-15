from mega_api.models import Ball, MegaBall


class BallUtils():

    @staticmethod
    def get_ball_by_number(value: str | int) -> Ball:
        number: int = int(value)
        referenced_ball: Ball = Ball.objects.get(number=number)
        if referenced_ball is None:
            raise Exception(Ball.DoesNotExist)
        else:
            return referenced_ball

    @staticmethod
    def get_mega_ball_by_number(value: str | int) -> MegaBall:
        number: int = int(value)
        referenced_ball: MegaBall = MegaBall.objects.get(number=number)
        if referenced_ball is None:
            raise Exception(MegaBall.DoesNotExist)
        return referenced_ball
