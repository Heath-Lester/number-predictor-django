"""Module for Winnning Set Model"""
"""Module for Winning Set Model"""
from django.db import models
from .number import Number

class Winning_Set(models.Model):
    """Winning Set Model"""
 
    first_number = models.ForeignKey(Number, on_delete=models.RESTRICT, related_name="First Number+")
    second_number = models.ForeignKey(Number, on_delete=models.RESTRICT, related_name="Second Number+")
    third_number = models.ForeignKey(Number, on_delete=models.RESTRICT, related_name="Third Number+")
    fourth_number = models.ForeignKey(Number, on_delete=models.RESTRICT, related_name="Fourth Number+")
    fifth_number = models.ForeignKey(Number, on_delete=models.RESTRICT, related_name="Fifth Number+")
    sixth_number = models.ForeignKey(Number, on_delete=models.RESTRICT, related_name="Sixth Number+")
    megaplier = models.PositiveSmallIntegerField() 
    date = models.DateField(auto_now=False, auto_now_add=False)
