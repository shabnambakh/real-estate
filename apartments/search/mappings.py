from elasticsearch_dsl import Integer, Text, Boolean

from search.mappings import BaseDocType
from ..models import Apartment


class ApartmentDoc(BaseDocType):
    rooms = Text()
    balcony_type = Text()
    army_mortgage = Boolean()
    mortgage = Boolean()
    price = Integer()
    area = Integer()
    city = Integer()

    class Meta:
        index = BaseDocType.search_index
        doc_type = 'apartment'

    @staticmethod
    def get_model():
        return Apartment
