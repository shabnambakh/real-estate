from elasticsearch.exceptions import RequestError
from elasticsearch_dsl import Index
from django.conf import settings
from django.utils.module_loading import import_string

from .mappings import BaseDocType


def get_doc_mappings():
    mappings = {}

    for path in settings.MAPPINGS:
        _class = import_string(path)
        mappings[_class.get_model()] = _class
    return mappings


def drop_index():
    index = _get_index()

    if index.exists():
        index.delete()


def open_index():
    index = _get_index()

    if index.exists():
        index.open()


def refresh_index():
    index = _get_index()
    index.refresh()


def update_index_settings():
    index = _get_index()

    index.settings(**{
        'max_result_window': 40000,
    })
    index.save()


def update_index_mapping():
    index = _get_index()

    try:
        index.settings(refresh_interval=-1)
        index.save()
        _update_mapping()
    except RequestError:
        pass
    finally:
        index.settings(refresh_interval='1s')
        index.save()


def rebuild_index():
    refresh_index()

    index = _get_index()
    try:
        index.settings(refresh_interval=-1)
        index.save()

        for doc in get_doc_mappings():
            doc.rebuild_index()

    finally:
        index.settings(refresh_interval='1s')
        index.save()

    refresh_index()


def _get_index():
    index = Index(BaseDocType.search_index)

    try:
        index.create()
    except RequestError as e:
        pass

    return index


def _update_mapping():
    index = _get_index()

    if not index.exists():
        index.create()

    index.close()

    for _class in get_doc_mappings():
        _class.init()

    index.open()
