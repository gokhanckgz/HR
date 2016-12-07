import django_tables2 as tables
from django_tables2.utils import A
from .models import Service

class ServiceTable(tables.Table):
    delete = tables.LinkColumn('service_delete', text='delete', args=[A('id')])
    edit = tables.LinkColumn('service_edit', text='edit', args=[A('id')])
    class Meta:
        model = Service
        attrs = {'class': 'paleblue'}
        fields = ('service_name', 'service_info',)
