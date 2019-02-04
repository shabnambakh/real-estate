from elasticsearch_dsl.query import Q


class SearchManager:
    doc_type = None
    model = None

    def do_search(self, filters):
        assert self.doc_type is not None, f'"{self.__class__.__name__}" should set a `doc_type` attribute'
        assert self.model is not None, f'"{self.__class__.__name__}" should set a `model` attribute'

        data = self.prepare_filters(filters)
        return self.execute_query(data)

    def execute_query(self, data):
        return []

    def prepare_filters(self, filters):
        return {
            key: value
            for key, value in filters.items()
            if value
        }

    def get_filters(self, data):
        return []


class ModelSearchManager(SearchManager):
    def execute_query(self, data):
        page = int(data.get('page', 1))
        page_size = int(data.get('pageSize', int(data.get('page_size', 100))))

        query = self.build_query(data) \
            .source('id')

        result = query[(page - 1) * page_size:page * page_size].execute()

        ids = [int(item.meta.id) for item in result]
        items = list(self.model.objects.filter(id__in=ids))
        items.sort(key=lambda i: ids.index(i.id))

        return items

    def build_query(self, data):
        return self.doc_type.search().query(Q(
            'bool',
            filter=self.get_filters(data)
        ))
