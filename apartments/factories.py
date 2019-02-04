import factory

from common.models import City
from .models import Apartment


class ApartmentFactory(factory.django.DjangoModelFactory):
    city = factory.Iterator(City.objects.all())
    price = factory.Faker('random_int', min=1000000, max=300000000)
    area = factory.Faker('random_int', min=18, max=41)
    rooms = factory.Faker('word', ext_word_list=[key for key, _ in Apartment.ROOMS])
    balcony_type = factory.Faker('word', ext_word_list=[key for key, _ in Apartment.BALCONY_TYPES])
    mortgage = factory.Faker('pybool')
    army_mortgage = factory.Faker('pybool')

    class Meta:
        model = Apartment
