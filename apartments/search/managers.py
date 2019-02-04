from elasticsearch_dsl import A
from elasticsearch_dsl.query import Q, Term, Terms, Range

from search.managers import SearchManager, ModelSearchManager
from ..models import Apartment
from .mappings import ApartmentDoc


def get_filters(data):
    filters = []

    if 'price_min' in data:
        filters.append(Range(price={"gte": data['price_min']}))

    if 'price_max' in data:
        filters.append(Range(price={"lte": data['price_max']}))

    if 'area_min' in data:
        filters.append(Range(area={"gte": data['area_min']}))

    if 'area_max' in data:
        filters.append(Range(area={"lte": data['area_max']}))

    if 'rooms' in data:
        filters.append(Terms(rooms=data['rooms'].split(',')))

    if 'city' in data:
        filters.append(Term(city=data['city']))

    if 'balcony_type' in data:
        filters.append(Terms(balcony_type=data['balcony_type'].split(',')))

    if data.get('mortgage', False):
        filters.append(Term(mortgage=False))

    if data.get('army_mortgage', False):
        filters.append(Term(army_mortgage=False))

    return filters


class ApartmentSearchManager(ModelSearchManager):
    doc_type = ApartmentDoc
    model = Apartment
    name = 'apartments'

    def get_filters(self, data):
        return get_filters(data)


class OptionSearchManager(SearchManager):
    doc_type = ApartmentDoc
    model = Apartment
    name = 'apartments'

    def get_filters(self, data):
        return get_filters(data)

    def get_filters_for_stats(self, data):
        filters = []
        if 'rooms' in data:
            filters.append(Terms(rooms=data['rooms'].split(',')))

        if 'city' in data:
            filters.append(Term(city=data['city']))

        return filters

    def execute_query(self, data):
        count = self.get_count(data)
        stats = self.get_stats(data)

        return {'min_price': stats.min_price.value,
                'max_price': stats.max_price.value,
                'min_area': stats.min_area.value,
                'max_area': stats.max_area.value,
                'count': count}

    def get_count(self, data):
        search = self.doc_type.search()
        query = search.query(Q(
            'bool', filter=self.get_filters(data)))

        return query.count()

    def get_stats(self, data):
        search = self.doc_type.search()
        query = search.query(Q(
            'bool', filter=self.get_filters_for_stats(data)))

        a1 = A('min', field='price')
        a2 = A('max', field='price')
        a3 = A('min', field='area')
        a4 = A('max', field='area')

        query.aggs.bucket('min_price', a1)
        query.aggs.bucket('max_price', a2)
        query.aggs.bucket('min_area', a3)
        query.aggs.bucket('max_area', a4)

        return query.execute().aggregations
