"""Module for Predictive Set Model"""
from django.db import models
from .number import Number

class Predictive_Set(models.Model):
    """Predictive Set Model"""
 
    first_number = models.PositiveSmallIntegerField()
    second_number = models.PositiveSmallIntegerField()
    third_number = models.PositiveSmallIntegerField()
    fourth_number = models.PositiveSmallIntegerField()
    fifth_number = models.PositiveSmallIntegerField()
    sixth_number = models.PositiveSmallIntegerField()
    megaplier = models.PositiveSmallIntegerField()
    date = models.DateField(auto_now=True, auto_now_add=True)
