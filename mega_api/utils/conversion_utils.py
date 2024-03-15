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
    def convert_megaplier_to_int(megaplier: str) -> int:
        megaplier = megaplier.replace('x', '')
        megaplier = megaplier.replace('X', '')
        return int(megaplier)

    @staticmethod
    def convert_number_string_to_int(number_string: str) -> int:
        number_string = number_string.replace(',', '')
        return int(number_string)

    @staticmethod
    def convert_date_string_to_date(date_string: str) -> date:
        print("DATE STRING: ", date_string)
        month, day, year = date_string.split("/")
        return date(month=int(month), day=int(day), year=int(year))

    @staticmethod
    def convert_alt_date_string_to_date(date_string: str) -> date:
        day_name, month_name_and_day, year = date_string.split(",")
        month_name, day = month_name_and_day.split(" ")
        month = ConversionUtils().get_month_number_from_mont_name(month_name)
        return date(month=int(month), day=int(day), year=int(year))

    @staticmethod
    def get_month_number_from_mont_name(month: str) -> int:
        match month:
            case 'January':
                return 1
            case 'February':
                return 2
            case 'March':
                return 3
            case 'April':
                return 4
            case 'May':
                return 5
            case 'June':
                return 6
            case 'July':
                return 7
            case 'August':
                return 8
            case 'September':
                return 9
            case 'October':
                return 10
            case 'November':
                return 11
            case 'December':
                return 12
            case _:
                raise ValueError('string is not a month name')
