from django.db import models
from search.mixins import Searchable


class Apartment(Searchable):
    BALCONY_TYPES = (
        ('1b', 'Балкон'),
        ('1l', 'Лоджия'),
        ('1b1l', 'Балкон и лоджия')
    )

    ROOMS = (
        ('studio', 'Студия'),
        ('1', '1-комнатная квартира'),
        ('2', '2-комнатная квартира'),
        ('3', '3-комнатная квартира'),
        ('4', '4-комнатная квартира'),
        ('5', '5-комнатная квартира'),
        ('6', '6-комнатная квартира')
    )

    city = models.ForeignKey('common.City', verbose_name='City', related_name='apartments', on_delete=models.CASCADE)
    rooms = models.CharField(choices=ROOMS, max_length=10, verbose_name='Rooms')
    price = models.IntegerField(verbose_name='Price')
    area = models.IntegerField(verbose_name='Area')
    balcony_type = models.CharField(choices=BALCONY_TYPES, max_length=10, verbose_name='Rooms')
    mortgage = models.BooleanField(verbose_name='Mortgage')
    army_mortgage = models.BooleanField(verbose_name='Army Mortgage')

    def __str__(self):
        return f'rooms: {self.rooms} | price: {self.price} | area: {self.area} ' \
               f'| balcony_type: {self.balcony_type} | mortgage: {self.mortgage} | army_mortgage: {self.army_mortgage}'
