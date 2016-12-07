# tutorial/tables.py
import django_tables2 as tables
from company.models import Benefit
from django_tables2.utils import A
from django.utils.html import format_html


class ImageColumn(tables.Column):
    def render(self, value):
        return format_html('<img src="/media/{}" height="50" />', value)


class ServiceLeaveTable(tables.Table):
    image = ImageColumn('Image')
    leave = tables.LinkColumn('service_leave', text='leave', args=[A('id')])

    class Meta:
        model = Benefit
        attrs = {'class': 'paleblue'}
        fields = ('id','service_name','service_info' )