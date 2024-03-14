"""View for Winning Numbers"""
from datetime import date
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
from mega_api.models import Ball, MegaBall, WinningSet
from mega_api.serializers.winning_set_serializer import WinningSetSerializer
from django.http import HttpResponseServerError, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseNotAllowed
from mega_api.utils.mega_parser import MegaParser
from pdb import set_trace


class WinningSets(ViewSet):
    """Class containing CRUD operations for Winning Sets"""

    def list(self, request) -> Response:
        """Handles GET requests for all Winning Sets"""

        try:
            winning_sets: list[WinningSet] = WinningSet.objects.all()

            serializer = WinningSetSerializer(
                winning_sets, many=True, context={'request': request})

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as exception:
            return HttpResponseServerError(exception, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None) -> Response:
        """Handles DELETE requests for all Winning Sets"""

        try:
            winning_set: WinningSet = WinningSet.objects.get(pk=pk)

            winning_set.delete()

        except WinningSet.DoesNotExist as exception:
            return Response({'message': exception.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as exception:
            return HttpResponseServerError(exception, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None) -> Response:
        """Handles GET requests for a single winning set"""

        try:
            winning_set: WinningSet = WinningSet.objects.get(pk=pk)

            serializer = WinningSetSerializer(
                winning_set, context={'request': request})

            return Response(serializer.data, status=status.HTTP_200_OK)

        except WinningSet.DoesNotExist as exception:
            return Response({'message': exception.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as exception:
            return HttpResponseServerError(exception, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request) -> Response:
        """Handles POST requests for a new winning set"""

        try:
            if request.body is None:
                return HttpResponseBadRequest({'message': 'body must include set data'}, status=status.HTTP_400_BAD_REQUEST)

            new_set = WinningSet()

            set_date: int | None = request.body['date']
            if set_date is not None:
                new_date: date = date.fromtimestamp(set_date)
                new_set.date = new_date

            def parse_ball(ball: int | Ball | None) -> int:
                if ball is not None:
                    if isinstance(ball, int):
                        try:
                            referenced_ball = Ball.objects.get(number=ball)
                            id: int | None = referenced_ball['id']
                            if id is not None:
                                return id
                            else:
                                raise HttpResponseServerError(
                                    {'message': 'retrieved ball ID is invalid'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                        except Ball.DoesNotExist as ex:
                            raise HttpResponseNotFound(
                                {'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
                        except Exception as ex:
                            raise HttpResponseServerError(
                                ex, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                    elif isinstance(ball, Ball):
                        id: int | None = ball['id']
                        if id is not None:
                            return id
                        else:
                            raise HttpResponseBadRequest(
                                {'message': 'ball ID is invalid'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    raise HttpResponseBadRequest(
                        {'message': 'ball is invalid'}, status=status.HTTP_400_BAD_REQUEST)

            def parse_mega_ball(ball: int | MegaBall | None) -> int:
                if ball is not None:
                    if isinstance(ball, int):
                        try:
                            referenced_ball = MegaBall.objects.get(number=ball)
                            id: int | None = referenced_ball['id']
                            if id is not None:
                                return id
                            else:
                                raise HttpResponseServerError(
                                    {'message': 'retrieved ball ID is invalid'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                        except MegaBall.DoesNotExist as ex:
                            raise HttpResponseNotFound(
                                {'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
                        except Exception as ex:
                            raise HttpResponseServerError(
                                ex, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                    elif isinstance(ball, MegaBall):
                        id: int | None = ball['id']
                        if id is not None:
                            return id
                        else:
                            raise HttpResponseBadRequest(
                                {'message': 'mega ball ID is invalid'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    raise HttpResponseBadRequest(
                        {'message': 'mega ball is invalid'}, status=status.HTTP_400_BAD_REQUEST)

            new_set.first_ball = parse_ball(request.data['first_ball'])

            new_set.second_ball = parse_ball(request.data['second_ball'])

            new_set.third_ball = parse_ball(request.data['third_ball'])

            new_set.fourth_ball = parse_ball(request.data['fourth_ball'])

            new_set.fifth_ball = parse_ball(request.data['fifth_ball'])

            new_set.mega_ball = parse_mega_ball(request.data['mega_ball'])

            megaplier: int | None = request.data['megaplier']
            if megaplier is not None and isinstance(megaplier, int):
                new_set.megaplier = megaplier
                return HttpResponseBadRequest({'message': 'megaplier is invalid'}, status=status.HTTP_400_BAD_REQUEST)

            estimated_jackpot: int | None = request.data['estimated_jackpot']
            if estimated_jackpot is not None and isinstance(estimated_jackpot, int):
                new_set.estimated_jackpot = estimated_jackpot

            cash_option: int | None = request.data['cash_option']
            if cash_option is not None and isinstance(cash_option, int):
                new_set.cash_option = cash_option

            five_match_prize: int | None = request.data['five_match_prize']
            if five_match_prize is not None and isinstance(five_match_prize, int):
                new_set.five_match_prize = five_match_prize

            four_w_mega_match_prize: int | None = request.data['four_w_mega_match_prize']
            if four_w_mega_match_prize is not None and isinstance(four_w_mega_match_prize, int):
                new_set.four_w_mega_match_prize = four_w_mega_match_prize

            four_match_prize: int | None = request.data['four_match_prize']
            if four_match_prize is not None and isinstance(four_match_prize, int):
                new_set.four_match_prize = four_match_prize

            three_w_mega_match_prize: int | None = request.data['three_w_mega_match_prize']
            if three_w_mega_match_prize is not None and isinstance(three_w_mega_match_prize, int):
                new_set.three_w_mega_match_prize

            three_match_prize: int | None = request.data['three_match_prize']
            if three_match_prize is not None and isinstance(three_match_prize, int):
                new_set.three_match_prize = three_match_prize

            two_w_mega_match_prize: int | None = request.data['two_w_mega_match_prize']
            if two_w_mega_match_prize is not None and isinstance(two_w_mega_match_prize, int):
                new_set.two_w_mega_match_prize = two_w_mega_match_prize

            one_w_mega_match_prize: int | None = request.data['one_w_mega_match_prize']
            if one_w_mega_match_prize is not None and isinstance(one_w_mega_match_prize, int):
                new_set.two_w_mega_match_prize = two_w_mega_match_prize

            four_w_mega_matches: int | None = request.data['four_w_mega_matches']
            if four_w_mega_matches is not None and isinstance(four_w_mega_matches, int):
                new_set.four_w_mega_matches = four_w_mega_matches

            four_matches: int | None = request.data['four_matches']
            if four_matches is not None and isinstance(four_matches, int):
                new_set.four_matches = four_matches

            three_w_mega_matches: int | None = request.data['three_w_mega_matches']
            if three_w_mega_matches is not None and isinstance(three_w_mega_matches, int):
                new_set.three_w_mega_matches = three_w_mega_matches

            three_matches: int | None = request.data['three_matches']
            if three_matches is not None and isinstance(three_matches, int):
                new_set.three_matches = three_matches

            two_w_mega_matches: int | None = request.data['two_w_mega_matches']
            if two_w_mega_matches is not None and isinstance(two_w_mega_matches, int):
                new_set.two_w_mega_matches = two_w_mega_matches

            one_w_mega_matches: int | None = request.data['one_w_mega_matches']
            if one_w_mega_matches is not None and isinstance(one_w_mega_matches, int):
                new_set.one_w_mega_matches = one_w_mega_matches

            mega_matches: int | None = request.data['mega_matches']
            if mega_matches is not None and isinstance(mega_matches, int):
                new_set.mega_matches = mega_matches

            new_set.save()

            serializer = WinningSetSerializer(
                new_set, context={'request': request})

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as exception:
            return HttpResponseServerError(exception, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, pk=None) -> Response:
        """Handles PATCH requests for all Winning Sets"""
        return HttpResponseNotAllowed({'message': 'method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request: Request, pk=None) -> Response:
        """Handles PUT requests for Winning Sets"""
        try:
            winning_set = WinningSet.objects.get(pk=pk)
            if request.body is None:
                return HttpResponseBadRequest({'message': 'body must include set data'}, status=status.HTTP_400_BAD_REQUEST)

            set_date: int | None = request.body['date']
            if set_date is not None:
                new_date: date = date.fromtimestamp(set_date)
                winning_set.date = new_date

            def parse_ball(ball: int | Ball | None) -> int | None:
                if ball is not None:
                    if isinstance(ball, int):
                        try:
                            referenced_ball = Ball.objects.get(number=ball)
                            id: int | None = referenced_ball['id']
                            if id is not None:
                                return id
                            else:
                                raise HttpResponseServerError(
                                    {'message': 'retrieved ball ID is invalid'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                        except Ball.DoesNotExist as ex:
                            raise HttpResponseNotFound(
                                {'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
                        except Exception as ex:
                            raise HttpResponseServerError(
                                ex, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                    elif isinstance(ball, Ball):
                        id: int | None = ball['id']
                        if id is not None:
                            return id
                        else:
                            raise HttpResponseBadRequest(
                                {'message': 'ball ID is invalid'}, status=status.HTTP_400_BAD_REQUEST)

            def parse_mega_ball(ball: int | MegaBall | None) -> int | None:
                if ball is not None:
                    if isinstance(ball, int):
                        try:
                            referenced_ball = MegaBall.objects.get(number=ball)
                            id: int | None = referenced_ball['id']
                            if id is not None:
                                return id
                            else:
                                raise HttpResponseServerError(
                                    {'message': 'retrieved ball ID is invalid'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                        except MegaBall.DoesNotExist as ex:
                            raise HttpResponseNotFound(
                                {'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
                        except Exception as ex:
                            raise HttpResponseServerError(
                                ex, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                    elif isinstance(ball, MegaBall):
                        id: int | None = ball['id']
                        if id is not None:
                            return id
                        else:
                            raise HttpResponseBadRequest(
                                {'message': 'mega ball ID is invalid'}, status=status.HTTP_400_BAD_REQUEST)

            first_ball: int | None = parse_ball(request.data['first_ball'])
            if first_ball is not None:
                winning_set.first_ball = first_ball

            second_ball: int | None = parse_ball(request.data['second_ball'])
            if second_ball is not None:
                winning_set.second_ball = second_ball

            third_ball: int | None = parse_ball(request.data['third_ball'])
            if third_ball is not None:
                winning_set.third_ball = third_ball

            fourth_ball: int | None = parse_ball(request.data['fourth_ball'])
            if fourth_ball is not None:
                winning_set.fourth_ball = fourth_ball

            fifth_ball: int | None = parse_ball(request.data['fifth_ball'])
            if fifth_ball is not None:
                winning_set.fifth_ball = fifth_ball

            mega_ball: int | None = parse_mega_ball(request.data['mega_ball'])
            if mega_ball is not None:
                winning_set.mega_ball = mega_ball

            megaplier: int | None = request.data['megaplier']
            if megaplier is not None and isinstance(megaplier, int):
                winning_set.megaplier = megaplier

            estimated_jackpot: int | None = request.data['estimated_jackpot']
            if estimated_jackpot is not None and isinstance(estimated_jackpot, int):
                winning_set.estimated_jackpot = estimated_jackpot

            cash_option: int | None = request.data['cash_option']
            if cash_option is not None and isinstance(cash_option, int):
                winning_set.cash_option = cash_option

            five_match_prize: int | None = request.data['five_match_prize']
            if five_match_prize is not None and isinstance(five_match_prize, int):
                winning_set.five_match_prize = five_match_prize

            four_w_mega_match_prize: int | None = request.data['four_w_mega_match_prize']
            if four_w_mega_match_prize is not None and isinstance(four_w_mega_match_prize, int):
                winning_set.four_w_mega_match_prize = four_w_mega_match_prize

            four_match_prize: int | None = request.data['four_match_prize']
            if four_match_prize is not None and isinstance(four_match_prize, int):
                winning_set.four_match_prize = four_match_prize

            three_w_mega_match_prize: int | None = request.data['three_w_mega_match_prize']
            if three_w_mega_match_prize is not None and isinstance(three_w_mega_match_prize, int):
                winning_set.three_w_mega_match_prize

            three_match_prize: int | None = request.data['three_match_prize']
            if three_match_prize is not None and isinstance(three_match_prize, int):
                winning_set.three_match_prize = three_match_prize

            two_w_mega_match_prize: int | None = request.data['two_w_mega_match_prize']
            if two_w_mega_match_prize is not None and isinstance(two_w_mega_match_prize, int):
                winning_set.two_w_mega_match_prize = two_w_mega_match_prize

            one_w_mega_match_prize: int | None = request.data['one_w_mega_match_prize']
            if one_w_mega_match_prize is not None and isinstance(one_w_mega_match_prize, int):
                winning_set.two_w_mega_match_prize = two_w_mega_match_prize

            four_w_mega_matches: int | None = request.data['four_w_mega_matches']
            if four_w_mega_matches is not None and isinstance(four_w_mega_matches, int):
                winning_set.four_w_mega_matches = four_w_mega_matches

            four_matches: int | None = request.data['four_matches']
            if four_matches is not None and isinstance(four_matches, int):
                winning_set.four_matches = four_matches

            three_w_mega_matches: int | None = request.data['three_w_mega_matches']
            if three_w_mega_matches is not None and isinstance(three_w_mega_matches, int):
                winning_set.three_w_mega_matches = three_w_mega_matches

            three_matches: int | None = request.data['three_matches']
            if three_matches is not None and isinstance(three_matches, int):
                winning_set.three_matches = three_matches

            two_w_mega_matches: int | None = request.data['two_w_mega_matches']
            if two_w_mega_matches is not None and isinstance(two_w_mega_matches, int):
                winning_set.two_w_mega_matches = two_w_mega_matches

            one_w_mega_matches: int | None = request.data['one_w_mega_matches']
            if one_w_mega_matches is not None and isinstance(one_w_mega_matches, int):
                winning_set.one_w_mega_matches = one_w_mega_matches

            mega_matches: int | None = request.data['mega_matches']
            if mega_matches is not None and isinstance(mega_matches, int):
                winning_set.mega_matches = mega_matches

            winning_set.save()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except WinningSet.DoesNotExist as exception:
            return Response({'message': exception.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as exception:
            return HttpResponseServerError(exception, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['post'], detail=True)
    def html(self, request: Request) -> Response:
        """Handles POST requests for parsing HTML from Mega Millions"""
        print("REQUEST: ", request)

        if request.method != "POST":
            return HttpResponseNotAllowed(permitted_methods=['POST'], status=status.HTTP_405_METHOD_NOT_ALLOWED)

        if request.body is None:
            return HttpResponseBadRequest({'message': 'body is invalid'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            set_trace()
            mega_parser = MegaParser()
            mega_parser.feed(request.body)
            data: list[str] = mega_parser.get_data()
            print('DATA: ', data)
            parsed_sets: list[WinningSet] = mega_parser.get_sets()
            saved_sets: list[WinningSet] = []

            for parsed_set in parsed_sets:
                existing_set = WinningSet.objects.get(date=parsed_set.date)
                if existing_set is None:
                    parsed_set.save()
                    saved_sets.append(parsed_set)
                else:
                    if existing_set.first_ball is None and parsed_set.first_ball is not None:
                        existing_set.first_ball = parsed_set.first_ball

                    if existing_set.second_ball is None and parsed_set.second_ball is not None:
                        existing_set.second_ball = parsed_set.second_ball

                    if existing_set.third_ball is None and parsed_set.third_ball is not None:
                        existing_set.first_ball = parsed_set.third_ball

                    if existing_set.fourth_ball is None and parsed_set.fourth_ball is not None:
                        existing_set.fourth_ball = parsed_set.fourth_ball

                    if existing_set.fifth_ball is None and parsed_set.fifth_ball is not None:
                        existing_set.fifth_ball = parsed_set.fifth_ball

                    if existing_set.mega_ball is None and parsed_set.mega_ball is not None:
                        existing_set.mega_ball = parsed_set.mega_ball

                    if existing_set.megaplier is None and parsed_set.megaplier is not None:
                        existing_set.megaplier = parsed_set.megaplier

                    # Standard Winners
                    if existing_set.jackpot_winners is None and parsed_set.jackpot_winners is not None:
                        existing_set.jackpot_winners = parsed_set.jackpot_winners

                    if existing_set.five_match_winners is None and parsed_set.five_match_winners is not None:
                        existing_set.five_match_winners = parsed_set.five_match_winners

                    if existing_set.four_match_w_mega_winners is None and parsed_set.four_match_w_mega_winners is not None:
                        existing_set.four_match_w_mega_winners = parsed_set.four_match_w_mega_winners

                    if existing_set.four_match_winners is None and parsed_set.four_match_winners is not None:
                        existing_set.four_match_winners = parsed_set.four_match_winners

                    if existing_set.three_match_w_mega_winners is None and parsed_set.three_match_w_mega_winners is not None:
                        existing_set.three_match_w_mega_winners = parsed_set.three_match_w_mega_winners

                    if existing_set.three_match_winners is None and parsed_set.three_match_winners is not None:
                        existing_set.three_match_winners = parsed_set.three_match_winners

                    if existing_set.two_match_w_mega_winners is None and parsed_set.two_match_w_mega_winners is not None:
                        existing_set.two_match_w_mega_winners = parsed_set.two_match_w_mega_winners

                    if existing_set.one_match_w_mega_winners is None and parsed_set.one_match_w_mega_winners is not None:
                        existing_set.one_match_w_mega_winners = parsed_set.one_match_w_mega_winners

                    if existing_set.mega_match_winners is None and parsed_set.mega_match_winners is not None:
                        existing_set.mega_match_winners = parsed_set.mega_match_winners

                    # Standard Prizes
                    if existing_set.estimated_jackpot is None and parsed_set.estimated_jackpot is not None:
                        existing_set.estimated_jackpot = parsed_set.estimated_jackpot

                    if existing_set.cash_option is None and parsed_set.cash_option is not None:
                        existing_set.cash_option = parsed_set.cash_option

                    if existing_set.five_match_prize is None and parsed_set.five_match_prize is not None:
                        existing_set.five_match_prize = parsed_set.five_match_prize

                    if existing_set.four_match_w_mega_prize is None and parsed_set.four_match_w_mega_prize is not None:
                        existing_set.four_match_w_mega_prize = parsed_set.four_match_w_mega_prize

                    if existing_set.four_match_prize is None and parsed_set.four_match_prize is not None:
                        existing_set.four_match_prize = parsed_set.four_match_prize

                    if existing_set.three_match_w_mega_prize is None and parsed_set.three_match_w_mega_prize is not None:
                        existing_set.three_match_w_mega_prize = parsed_set.three_match_w_mega_prize

                    if existing_set.three_match_prize is None and parsed_set.three_match_prize is not None:
                        existing_set.three_match_prize = parsed_set.three_match_prize

                    if existing_set.two_match_w_mega_prize is None and parsed_set.two_match_w_mega_prize is not None:
                        existing_set.two_match_w_mega_prize = parsed_set.two_match_w_mega_prize

                    if existing_set.one_match_w_mega_prize is None and parsed_set.one_match_w_mega_prize is not None:
                        existing_set.one_match_w_mega_prize = parsed_set.one_match_w_mega_prize

                    if existing_set.mega_match_prize is None and parsed_set.mega_match_prize is not None:
                        existing_set.mega_match_prize = parsed_set.mega_match_prize

                    # Megaplier Winners
                    if existing_set.jackpot_megaplier_winners is None and parsed_set.jackpot_megaplier_winners is not None:
                        existing_set.jackpot_megaplier_winners = parsed_set.jackpot_megaplier_winners

                    if existing_set.five_match_megaplier_winners is None and parsed_set.five_match_megaplier_winners is not None:
                        existing_set.five_match_megaplier_winners = parsed_set.five_match_megaplier_winners

                    if existing_set.four_match_w_mega_megaplier_winners is None and parsed_set.four_match_w_mega_megaplier_winners is not None:
                        existing_set.four_match_w_mega_megaplier_winners = parsed_set.four_match_w_mega_megaplier_winners

                    if existing_set.four_match_megaplier_winners is None and parsed_set.four_match_megaplier_winners is not None:
                        existing_set.four_match_megaplier_winners = parsed_set.four_match_megaplier_winners

                    if existing_set.three_match_w_mega_megaplier_winners is None and parsed_set.three_match_w_mega_megaplier_winners is not None:
                        existing_set.three_match_w_mega_megaplier_winners = parsed_set.three_match_w_mega_megaplier_winners

                    if existing_set.three_match_megaplier_winners is None and parsed_set.three_match_megaplier_winners is not None:
                        existing_set.three_match_megaplier_winners = parsed_set.three_match_megaplier_winners

                    if existing_set.two_match_w_mega_megaplier_winners is None and parsed_set.two_match_w_mega_megaplier_winners is not None:
                        existing_set.two_match_w_mega_megaplier_winners = parsed_set.two_match_w_mega_megaplier_winners

                    if existing_set.one_match_w_mega_megaplier_winners is None and parsed_set.one_match_w_mega_megaplier_winners is not None:
                        existing_set.one_match_w_mega_megaplier_winners = parsed_set.one_match_w_mega_megaplier_winners

                    if existing_set.mega_match_megaplier_winners is None and parsed_set.mega_match_megaplier_winners is not None:
                        existing_set.mega_match_megaplier_winners = parsed_set.mega_match_megaplier_winners

                    # Megaplier Prizes
                    if existing_set.five_match_megaplier_prize is None and parsed_set.five_match_megaplier_prize is not None:
                        existing_set.five_match_megaplier_prize = parsed_set.five_match_megaplier_prize

                    if existing_set.four_match_w_mega_megaplier_prize is None and parsed_set.four_match_w_mega_megaplier_prize is not None:
                        existing_set.four_match_w_mega_megaplier_prize = parsed_set.four_match_w_mega_megaplier_prize

                    if existing_set.four_match_megaplier_prize is None and parsed_set.four_match_megaplier_prize is not None:
                        existing_set.four_match_megaplier_prize = parsed_set.four_match_megaplier_prize

                    if existing_set.three_match_w_mega_megaplier_prize is None and parsed_set.three_match_w_mega_megaplier_prize is not None:
                        existing_set.three_match_w_mega_megaplier_prize = parsed_set.three_match_w_mega_megaplier_prize

                    if existing_set.three_match_megaplier_prize is None and parsed_set.three_match_megaplier_prize is not None:
                        existing_set.three_match_megaplier_prize = parsed_set.three_match_megaplier_prize

                    if existing_set.two_match_w_mega_megaplier_prize is None and parsed_set.two_match_w_mega_megaplier_prize is not None:
                        existing_set.two_match_w_mega_megaplier_prize = parsed_set.two_match_w_mega_megaplier_prize

                    if existing_set.one_match_w_mega_megaplier_prize is None and parsed_set.one_match_w_mega_megaplier_prize is not None:
                        existing_set.one_match_w_mega_megaplier_prize = parsed_set.one_match_w_mega_megaplier_prize

                    if existing_set.mega_match_megaplier_prize is None and parsed_set.mega_match_megaplier_prize is not None:
                        existing_set.mega_match_megaplier_prize = parsed_set.mega_match_megaplier_prize

                    existing_set.save()
                    saved_sets.append(existing_set)

            serializer = WinningSetSerializer(
                saved_sets, many=True, context={'request': request})

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as exception:
            return HttpResponseServerError(exception, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
