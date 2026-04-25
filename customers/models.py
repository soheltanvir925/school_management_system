from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

# Create your models here.
class Client(TenantMixin):
    name = models.CharField(max_length=100)
    on_trial = models.BooleanField(default=True)
    paid_until = models.DateField()
    create_on = models.DateField(auto_now_add=True)

    auto_create_schema = True

class Domain(DomainMixin):
    pass