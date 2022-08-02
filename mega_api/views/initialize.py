from curses.ascii import isalnum
from datetime import date, datetime
from operator import concat
from django.views.decorators.csrf import csrf_exempt
from data_extractions import *
from mega_api.models.number import Number
from mega_api.models.winning_set import Winning_Set


@csrf_exempt
def initialize(request):

    data_extraction = open("07312022.html", "r").read()

    print("DATA EXTRACTION", data_extraction)

    data_sets = data_extraction.split("</a>")

    print("DATA SETS", data_sets)

    for set in data_sets:

        new_winning_set = Winning_Set()

        new_first_number = Number()
        new_second_number = Number()
        new_third_number = Number()
        new_fourth_number = Number()
        new_fifth_number = Number()
        new_sixth_number = Number()
        new_megaplier = Number()

        new_first_number.position = 1
        new_second_number.position = 2
        new_third_number.position = 3
        new_fourth_number.position = 4
        new_fifth_number.position = 5
        new_sixth_number.position = 6
        new_megaplier.position = 7
        
        date_string_index = set.index('?date=') + 6
        date_string_rindex = date_string_index + 18
        
        date_string = set[date_string_index: date_string_rindex]
        
        if date_string.isdigit():
            new_winning_set.date = date.strftime(date_string, "MM-DD-YYYY")
            
        else:
            raw_date_string_index = set.index('<h5 class="drawItemDate">') + 25
            raw_date_string_rindex = raw_date_string_index + 10
            
            raw_date_string = set[raw_date_string_index: raw_date_string_rindex]
            
            if raw_date_string.endswith('<') or raw_date_string.endswith('/'):
                
                raw_date_list = raw_date_string.split('/')
                
                new_winning_set.date = date.strftime(concat(raw_date_list[0],'/', raw_date_list[1], '/', raw_date_list[2][0:3]), 'MM-DD-YYYY')
            
            else:
                new_winning_set.date = date.strftime(raw_date_string, 'MM-DD-YYYY')
                
        
            
        
        
