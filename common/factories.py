import factory

from .models import City


class CityFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('city')

    class Meta:
        model = City
