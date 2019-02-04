from django.db import models, transaction
from .tasks import update_object_search_index


class Searchable(models.Model):
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_search_index()

    def update_search_index(self):
        transaction.on_commit(lambda: update_object_search_index.delay(
            obj_id=self.id,
            app_label=self._meta.app_label,
            model=self._meta.model_name
        ))

    class Meta:
        abstract = True
