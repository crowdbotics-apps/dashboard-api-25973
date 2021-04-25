from datetime import datetime
import uuid

from django.contrib.auth import get_user_model
from django.db import models

from dashboard.models.choices import AppTypeChoices, AppFrameWorkChoices, \
    PlanPriceChoices
from django.db.models.functions import Length


User = get_user_model()
models.CharField.register_lookup(Length)
models.TextField.register_lookup(Length)


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
    name: str = models.CharField(
        max_length=50,
    )
    description: str = models.TextField()
    type: str = models.CharField(
        max_length=6,
        choices=[(tag, tag.value) for tag in AppTypeChoices]
    )
    framework: str = models.CharField(
        max_length=12,
        choices=[(tag, tag.value) for tag in AppFrameWorkChoices]
    )
    domain_name: str = models.CharField(
        max_length=50
    )
    screenshot: str = models.URLField()
    user: int = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="apps"
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(name__length__gte=1),
                name="%(app_label)s_%(class)s_name_length",
            )
        ]


class Plan(BaseModelMixin):
    name: str = models.CharField(
        max_length=20
    )
    description: str = models.TextField()
    price: str = models.CharField(
        max_length=3,
        default=PlanPriceChoices.FREE,
        choices=[(tag, tag.value) for tag in PlanPriceChoices]
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(name__length__gte=1),
                name="%(app_label)s_%(class)s_name_length",
            ),
            models.CheckConstraint(
                check=models.Q(description__length__gte=1),
                name="%(app_label)s_%(class)s_description_length",
            )
        ]


class Subscription(BaseModelMixin):
    app = models.OneToOneField(
        App,
        on_delete=models.Case,
    )
    plan = models.ForeignKey(
        Plan,
        on_delete=models.CASCADE,
        related_name="subscriptions"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="subscriptions"
    )
