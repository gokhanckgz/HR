# tutorial/tables.py
import django_tables2 as tables
from supplier.models import Service
from django_tables2.utils import A
from django.utils.html import format_html
from company.models import Employe


class ImageColumn(tables.Column):
    def render(self, value ,):
        return format_html('<img src="/media/{}" height="50" />', value)


class EmployeTable(tables.Table):
    delete = tables.LinkColumn('emp_delete', text='delete', args=[A('id')])
    edit = tables.LinkColumn('emp_edit', text='edit', args=[A('id')])
    image = ImageColumn('Image')

    class Meta:
        model = Employe
        attrs = {'class': 'paleblue'}
        fields = ('name','surname')


class ServiceTable(tables.Table):
    image = ImageColumn('Image')

    class Meta:
        model = Service
        attrs = {'class': 'paleblue'}
        fields = ('image', 'user_id', 'service_name', 'service_used', 'service_percent',)
