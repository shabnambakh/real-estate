from contextlib import suppress

from elasticsearch_dsl import DocType
from elasticsearch.exceptions import TransportError
from elasticsearch.helpers import bulk
from elasticsearch_dsl.connections import connections
from django.conf import settings
from django.db.models import ForeignKey


BULK_SIZE = 1000


class BaseDocType(DocType):
    search_index = settings.ELASTICSEARCH_INDEX

    @staticmethod
    def get_model():
        return None

    @classmethod
    def rebuild_index(cls):
        cls.search().query('match_all').delete()

        queryset = cls.index_queryset()
        total = queryset.count()
        if not total:
            return

        for obj in cls.queryset_iterator(queryset.all()):
            docs.append(cls.from_obj(obj))

            if len(docs) >= BULK_SIZE:
                cls._bulk_insert(docs)
                docs = []

            cls._bulk_insert(docs)

    @staticmethod
    def _bulk_insert(docs):
        bulk(connections.get_connection(), [d.to_dict(True) for d in docs])

    @classmethod
    def update_object_index(cls, obj):
        from .search_index import refresh_index

        cls.delete_object_index(obj.id)

        doc = cls.from_obj(obj)
        doc.save()

        refresh_index()

    @classmethod
    def delete_object_index(cls, obj_id):
        from .search_index import refresh_index

        with suppress(TransportError):
            old = cls.get(id=obj_id)
            old.delete()
            refresh_index()

    @classmethod
    def index_queryset(cls):
        model = cls.get_model()
        return model.objects.all()

    @classmethod
    def from_obj(cls, obj):
        doc = cls()
        doc.meta.id = obj.id

        props = [
            prop
            for prop in list(cls._doc_type.mapping.properties._params['properties'].keys())
        ]

        for prop in props:
            if hasattr(obj, prop):
                field = cls.get_model()._meta.get_field(prop)

                if isinstance(field, ForeignKey):
                    setattr(doc, prop, getattr(obj, prop).id)
                else:
                    setattr(doc, prop, getattr(obj, prop))
        return doc
