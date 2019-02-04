import celery
from django.contrib.contenttypes.models import ContentType

from real_estate.celery import app
from .search_index import get_doc_mappings


@app.task(base=celery.Task)
def update_object_search_index(obj_id, app_label, model):
    model_type = ContentType.objects.get_by_natural_key(app_label, model)
    _class = model_type.model_class()
    mappings = get_doc_mappings()
    mappings[_class].update_object_index(obj=_class.objects.get(id=obj_id))


@app.task(base=celery.Task)
def delete_object_from_search_index(obj_id, app_label, model):
    model_type = ContentType.objects.get_by_natural_key(app_label, model)
    mappings = get_doc_mappings()
    mappings[model_type.model_class()].delete_object_index(obj_id)

