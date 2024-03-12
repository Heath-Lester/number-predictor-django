from datetime import date


class ConversionUtils():

    @staticmethod
    def convert_dollar_to_int(dollars: str) -> int:
        dollars = dollars.replace('$', '')
        dollars = dollars.replace(',', '')
        if dollars.endswith('Million'):
            dollars.replace('Million', '')
            amount = int(dollars)
            return amount * 1000000
        else:
            return int(dollars)

    @staticmethod
    def convert_number_string_to_int(number_string: str) -> int:
        number_string = number_string.replace(',', '')
        return int(number_string)

    @staticmethod
    def convert_date_string_to_date(date_string: str) -> date:
        month, day, year = date_string.split("/")
        return date(month=month, day=day, year=year)
