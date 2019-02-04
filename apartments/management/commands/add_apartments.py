from core.commands import BaseAppCommand
from ...factories import ApartmentFactory


class Command(BaseAppCommand):
    default_size = 100
    factory_model = ApartmentFactory
