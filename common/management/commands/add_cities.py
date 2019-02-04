from core.commands import BaseAppCommand
from ...factories import CityFactory


class Command(BaseAppCommand):
    factory_model = CityFactory
