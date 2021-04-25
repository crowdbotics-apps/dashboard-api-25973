from datetime import datetime
import uuid
from django.db import models


class BaseModelMixin(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True,
                          primary_key=True)
    active = models.BooleanField(default=True)

    def soft_delete(self):
        self.deleted_at = datetime.utcnow()
        self.is_deleted = True
        self.active = False
        self.save()


class App(BaseModelMixin):
    pass


class Plan(BaseModelMixin):
    pass


class Subscription(BaseModelMixin):
    pass
