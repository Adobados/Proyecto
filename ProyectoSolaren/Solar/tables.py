import django_tables2 as tables
from Solar.models import inventario

class SimpleTable(tables.Table):
    class Meta:
        model = inventario
