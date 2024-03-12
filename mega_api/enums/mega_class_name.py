from enum import Enum


class MegaClassName(Enum):
    NONE = None
    DATE = 'drawItemDate'
    ALT_DATE = 'prevWinDate'
    FIRST_BALL = 'ball pastNum1'
    SECOND_BALL = 'ball pastNum2'
    THIRD_BALL = 'ball pastNum3'
    FOURTH_BALL = 'ball pastNum4'
    FIFTH_BALL = 'ball pastNum5'
    MEGA_BALL = 'ball yellowBall pastNumMB'
    MEGAPLIER = 'megaplier pastNumMP'
    # Standard Winners
    JACKPOT_WINNERS = 'dividerLine-small tier0 ie11-col2 ie11-row2'
    FIVE_MATCH_WINNERS = 'dividerLine-small tier1t ie11-col2 ie11-row3'
    FOUR_MATCH_W_MEGA_WINNERS = 'dividerLine-small tier2t ie11-col2 ie11-row4'
    FOUR_MATCH_WINNERS = 'dividerLine-small tier3t ie11-col2 ie11-row5'
    THREE_MATCH_W_MEGA_WINNERS = 'dividerLine-small tier4t ie11-col2 ie11-row6'
    THREE_MATCH_WINNERS = 'dividerLine-small tier5t ie11-col2 ie11-row7'
    TWO_MATCH_W_MEGA_WINNERS = 'dividerLine-small tier6t ie11-col2 ie11-row8'
    ONE_MATCH_W_MEGA_WINNERS = 'dividerLine-small tier7t ie11-col2 ie11-row9'
    MEGA_MATCH_WINNERS = 'dividerLine-small tier8t ie11-col2 ie11-row10'
    # Prizes
    ESTIMATED_JACKPOT = 'estJackpot js_pastJackpot'
    CASH_OPTION = 'nextCashOpt js_pastCashOpt'
    FIVE_MATCH_PRIZE = 'dividerLine-small prize1 ie11-col3 ie11-row3'
    FOUR_MATCH_W_MEGA_PRIZE = 'dividerLine-small prize2 ie11-col3 ie11-row4'
    FOUR_MATCH_PRIZE = 'dividerLine-small prize3 ie11-col3 ie11-row5'
    THREE_MATCH_W_MEGA_PRIZE = 'dividerLine-small prize4 ie11-col3 ie11-row6'
    THREE_MATCH_PRIZE = 'dividerLine-small prize5 ie11-col3 ie11-row7'
    TWO_MATCH_W_MEGA_PRIZE = 'dividerLine-small prize6 ie11-col3 ie11-row8'
    ONE_MATCH_W_MEGA_PRIZE = 'dividerLine-small prize7 ie11-col3 ie11-row9'
    MEGA_MATCH_PRIZE = 'dividerLine-small prize8 ie11-col3 ie11-row10'
    # Megaplier Winners
    FIVE_MATCH_MEGAPLIER_WINNERS = 'dividerLine-small tier1 ie11-col4 ie11-row3'
    FOUR_MATCH_W_MEGA_MEGAPLIER_WINNERS = 'dividerLine-small tier2 ie11-col4 ie11-row4'
    FOUR_MATCH_MEGAPLIER_WINNERS = 'dividerLine-small tier3 ie11-col4 ie11-row5'
    THREE_MATCH_W_MEGA_MEGAPLIER_WINNERS = 'dividerLine-small tier4 ie11-col4 ie11-row6'
    THREE_MATCH_MEGAPLIER_WINNERS = 'dividerLine-small tier5 ie11-col4 ie11-row7'
    TWO_MATCH_W_MEGA_MEGAPLIER_WINNERS = 'dividerLine-small tier6 ie11-col4 ie11-row8'
    ONE_MATCH_W_MEGA_MEGAPLIER_WINNERS = 'dividerLine-small tier7 ie11-col4 ie11-row9'
    MEGA_MATCH_MEGAPLIER_WINNERS = 'dividerLine-small tier8 ie11-col4 ie11-row10'
    # Megaplier Prizes
    FIVE_MATCH_MEGAPLIER_PRIZE = 'dividerLine-small endCell megPrize mPrize1 ie11-col5 ie11-row3'
    FOUR_MATCH_W_MEGA_MEGAPLIER_PRIZE = 'dividerLine-small endCell megPrize mPrize2 ie11-col5 ie11-row4'
    FOUR_MATCH_MEGAPLIER_PRIZE = 'dividerLine-small endCell megPrize mPrize3 ie11-col5 ie11-row5'
    THREE_MATCH_W_MEGA_MEGAPLIER_PRIZE = 'dividerLine-small endCell megPrize mPrize4 ie11-col5 ie11-row6'
    THREE_MATCH_MEGAPLIER_PRIZE = 'dividerLine-small endCell megPrize mPrize5 ie11-col5 ie11-row7'
    TWO_MATCH_W_MEGA_MEGAPLIER_PRIZE = 'dividerLine-small endCell megPrize mPrize6 ie11-col5 ie11-row8'
    ONE_MATCH_W_MEGA_MEGAPLIER_PRIZE = 'dividerLine-small endCell megPrize mPrize7 ie11-col5 ie11-row9'
    MEGA_MATCH_MEGAPLIER_PRIZE = 'dividerLine-small endCell megPrize mPrize8 ie11-col5 ie11-row10'

    @classmethod
    def has_matching_value(self, value: str | None) -> bool:
        class_values: list[str] = self._member_names_
        return value in class_values
