"""View for Skimming, Parsing, and Importing Web Data into SQLite Database"""

from datetime import date
from operator import concat
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework import status
from mega_api.models.ball import Ball
from mega_api.models.mega_ball import MegaBall
from mega_api.models.winning_set import WinningSet


@csrf_exempt
def initialize():
    """Imports data from the data_extractions folder"""

    data_extraction: str = open(
        "07312022.html", "r", encoding="utf-8").read()

    print("DATA EXTRACTION", data_extraction)

    data_sets: list[str] = data_extraction.split("</a>")

    print("DATA SETS", data_sets)

    sets: list[WinningSet] = []

    for data_set in data_sets:

        winning_set: WinningSet = WinningSet()

        first_ball: Ball = Ball()
        second_ball: Ball = Ball()
        third_ball: Ball = Ball()
        fourth_ball: Ball = Ball()
        fifth_ball: Ball = Ball()
        mega_ball: MegaBall = MegaBall()
        megaplier: int = 0

        date_string_index: int = data_set.index('?date=') + 6
        date_string_rindex: int = date_string_index + 18

        date_string: str = data_set[date_string_index: date_string_rindex]

        if date_string.isdigit():
            winning_set.date = date.strftime(date_string, "MM-DD-YYYY")

        else:
            raw_date_string_index: int = data_set.index(
                '<h5 class="drawItemDate">') + 25
            raw_date_string_rindex: int = raw_date_string_index + 10

            raw_date_string: str = data_set[raw_date_string_index: raw_date_string_rindex]

            if raw_date_string.endswith('<') or raw_date_string.endswith('/'):

                raw_date_list = raw_date_string.split('/')

                winning_set.date = date.strftime(
                    concat(
                        raw_date_list[0],
                        '/', raw_date_list[1],
                        '/', raw_date_list[2][0:3]),
                    'MM-DD-YYYY')

            else:
                winning_set.date = date.strftime(
                    raw_date_string, 'MM-DD-YYYY')

        winning_set.save()

        sets.append(winning_set)

    return HttpResponse(sets, content_type='application/json', status=status.HTTP_201_CREATED)
