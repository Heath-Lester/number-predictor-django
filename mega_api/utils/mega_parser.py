from html.parser import HTMLParser
from mega_api.enums.mega_class_name import MegaClassName
from mega_api.models import WinningSet
from mega_api.utils import BallUtils, ConversionUtils


class MegaParser(HTMLParser):

    current_attr: MegaClassName = MegaClassName.NONE
    parsed_sets: list[WinningSet] = []
    current_set = WinningSet()

    def __init__(self, *, convert_charrefs: bool = True) -> None:
        self.current_attr = MegaClassName.NONE
        self.parsed_sets = []
        self.current_set = WinningSet()
        super().__init__(convert_charrefs=convert_charrefs)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if len(attrs) == 0:
            self.current_attr = MegaClassName.NONE
        else:
            for key, value in attrs:
                if key == 'class':
                    if MegaClassName.has_matching_value(value):
                        self.current_attr = MegaClassName[MegaClassName.get_key_by_value(
                            value)]
                        break
                    else:
                        self.current_attr = MegaClassName.NONE

    def handle_data(self, data: str | None) -> None:
        if self.current_attr != MegaClassName.NONE and data is not None and len(data) > 0:
            if len(data) > 0:
                self.parsed_data.append(data)

                self.set_field(data)

                if self.current_attr == MegaClassName.MEGA_MATCH_MEGAPLIER_PRIZE or self.current_attr == MegaClassName.MEGAPLIER:
                    self.load_set()
        self.current_attr = MegaClassName.NONE

    def load_set(self) -> None:
        self.parsed_sets.append(self.current_set)
        self.current_set = WinningSet()

    def get_sets(self) -> list[WinningSet]:
        return self.parsed_sets.copy()

    def set_field(self, value: str) -> None:
        if len(value) > 0:
            match self.current_attr:
                case MegaClassName.NONE:
                    print('Class name is None')
                case MegaClassName.DATE:
                    self.current_set.date = ConversionUtils().convert_date_string_to_date(value)
                case MegaClassName.ALT_DATE:
                    self.current_set.date = ConversionUtils().convert_alt_date_string_to_date(value)
                case MegaClassName.FIRST_BALL:
                    self.current_set.first_ball = BallUtils.get_ball_by_number(
                        value)
                case MegaClassName.SECOND_BALL:
                    self.current_set.second_ball = BallUtils.get_ball_by_number(
                        value)
                case MegaClassName.THIRD_BALL:
                    self.current_set.third_ball = BallUtils.get_ball_by_number(
                        value)
                case MegaClassName.FOURTH_BALL:
                    self.current_set.fourth_ball = BallUtils.get_ball_by_number(
                        value)
                case MegaClassName.FIFTH_BALL:
                    self.current_set.fifth_ball = BallUtils.get_ball_by_number(
                        value)
                case MegaClassName.MEGA_BALL:
                    self.current_set.mega_ball = BallUtils.get_mega_ball_by_number(
                        value)
                case MegaClassName.MEGAPLIER:
                    self.current_set.megaplier = ConversionUtils().convert_megaplier_to_int(value)
                # Standard Winners
                case MegaClassName.JACKPOT_WINNERS:
                    self.current_set.jackpot_winners = ConversionUtils(
                    ).convert_number_string_to_int(value)
                case MegaClassName.FIVE_MATCH_WINNERS:
                    self.current_set.five_match_winners = ConversionUtils.convert_number_string_to_int(
                        value)
                case MegaClassName.FOUR_MATCH_W_MEGA_WINNERS:
                    self.current_set.four_match_w_mega_winners = ConversionUtils.convert_number_string_to_int(
                        value)
                case MegaClassName.FOUR_MATCH_WINNERS:
                    self.current_set.four_match_winners = ConversionUtils.convert_number_string_to_int(
                        value)
                case MegaClassName.THREE_MATCH_W_MEGA_WINNERS:
                    self.current_set.three_match_w_mega_winners = ConversionUtils.convert_number_string_to_int(
                        value)
                case MegaClassName.THREE_MATCH_WINNERS:
                    self.current_set.three_match_winners = ConversionUtils.convert_number_string_to_int(
                        value)
                case MegaClassName.TWO_MATCH_W_MEGA_WINNERS:
                    self.current_set.two_match_w_mega_winners = ConversionUtils.convert_number_string_to_int(
                        value)
                case MegaClassName.ONE_MATCH_W_MEGA_WINNERS:
                    self.current_set.one_match_w_mega_winners = ConversionUtils.convert_number_string_to_int(
                        value)
                case MegaClassName.MEGA_MATCH_WINNERS:
                    self.current_set.mega_match_winners = ConversionUtils.convert_number_string_to_int(
                        value)
                # Prizes
                case MegaClassName.ESTIMATED_JACKPOT:
                    self.current_set.estimated_jackpot = ConversionUtils().convert_dollar_to_int(value)
                case MegaClassName.CASH_OPTION:
                    self.current_set.cash_option = ConversionUtils().convert_dollar_to_int(value)
                case MegaClassName.FIVE_MATCH_PRIZE:
                    self.current_set.five_match_prize = ConversionUtils.convert_dollar_to_int(
                        value)
                case MegaClassName.FOUR_MATCH_W_MEGA_PRIZE:
                    self.current_set.four_match_w_mega_prize = ConversionUtils.convert_dollar_to_int(
                        value)
                case MegaClassName.FOUR_MATCH_PRIZE:
                    self.current_set.four_match_prize = ConversionUtils.convert_dollar_to_int(
                        value)
                case MegaClassName.THREE_MATCH_W_MEGA_PRIZE:
                    self.current_set.three_match_w_mega_prize = ConversionUtils.convert_dollar_to_int(
                        value)
                case MegaClassName.THREE_MATCH_PRIZE:
                    self.current_set.three_match_prize = ConversionUtils.convert_dollar_to_int(
                        value)
                case MegaClassName.TWO_MATCH_W_MEGA_PRIZE:
                    self.current_set.two_match_w_mega_prize = ConversionUtils.convert_dollar_to_int(
                        value)
                case MegaClassName.ONE_MATCH_W_MEGA_PRIZE:
                    self.current_set.one_match_w_mega_prize = ConversionUtils.convert_dollar_to_int(
                        value)
                case MegaClassName.MEGA_MATCH_PRIZE:
                    self.current_set.mega_match_prize = ConversionUtils.convert_dollar_to_int(
                        value)
                # Megaplier Winners
                case MegaClassName.FIVE_MATCH_MEGAPLIER_WINNERS:
                    self.current_set.five_match_megaplier_winners = ConversionUtils.convert_number_string_to_int(
                        value)
                case MegaClassName.FOUR_MATCH_W_MEGA_MEGAPLIER_WINNERS:
                    self.current_set.four_match_w_mega_megaplier_winners = ConversionUtils.convert_number_string_to_int(
                        value)
                case MegaClassName.FOUR_MATCH_MEGAPLIER_WINNERS:
                    self.current_set.four_match_megaplier_winners = ConversionUtils.convert_number_string_to_int(
                        value)
                case MegaClassName.THREE_MATCH_W_MEGA_MEGAPLIER_WINNERS:
                    self.current_set.three_match_w_mega_megaplier_winners = ConversionUtils.convert_number_string_to_int(
                        value)
                case MegaClassName.THREE_MATCH_MEGAPLIER_WINNERS:
                    self.current_set.three_match_megaplier_winners = ConversionUtils.convert_number_string_to_int(
                        value)
                case MegaClassName.TWO_MATCH_W_MEGA_MEGAPLIER_WINNERS:
                    self.current_set.two_match_w_mega_megaplier_winners = ConversionUtils.convert_number_string_to_int(
                        value)
                case MegaClassName.ONE_MATCH_W_MEGA_MEGAPLIER_WINNERS:
                    self.current_set.one_match_w_mega_megaplier_winners = ConversionUtils.convert_number_string_to_int(
                        value)
                case MegaClassName.MEGA_MATCH_MEGAPLIER_WINNERS:
                    self.current_set.mega_match_megaplier_winners = ConversionUtils.convert_number_string_to_int(
                        value)
                # Megaplier Prizes
                case MegaClassName.FIVE_MATCH_MEGAPLIER_PRIZE:
                    self.current_set.five_match_megaplier_prize = ConversionUtils.convert_dollar_to_int(
                        value)
                case MegaClassName.FOUR_MATCH_W_MEGA_MEGAPLIER_PRIZE:
                    self.current_set.four_match_w_mega_megaplier_prize = ConversionUtils.convert_dollar_to_int(
                        value)
                case MegaClassName.FOUR_MATCH_MEGAPLIER_PRIZE:
                    self.current_set.four_match_megaplier_prize = ConversionUtils.convert_dollar_to_int(
                        value)
                case MegaClassName.THREE_MATCH_W_MEGA_MEGAPLIER_PRIZE:
                    self.current_set.three_match_w_mega_megaplier_prize = ConversionUtils.convert_dollar_to_int(
                        value)
                case MegaClassName.THREE_MATCH_MEGAPLIER_PRIZE:
                    self.current_set.three_match_megaplier_prize = ConversionUtils.convert_dollar_to_int(
                        value)
                case MegaClassName.TWO_MATCH_W_MEGA_MEGAPLIER_PRIZE:
                    self.current_set.two_match_w_mega_megaplier_prize = ConversionUtils.convert_dollar_to_int(
                        value)
                case MegaClassName.ONE_MATCH_W_MEGA_MEGAPLIER_PRIZE:
                    self.current_set.one_match_w_mega_megaplier_prize = ConversionUtils.convert_dollar_to_int(
                        value)
                case MegaClassName.MEGA_MATCH_MEGAPLIER_PRIZE:
                    self.current_set.mega_match_megaplier_prize = ConversionUtils.convert_dollar_to_int(
                        value)
                case _:
                    print('Class name not handled: ', self.current_attr)
