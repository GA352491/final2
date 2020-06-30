import django_filters
from .models import *
from django_filters import DateFilter


class InvoiceFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_created', lookup_expr='gte')
    end_date = DateFilter(field_name='date_created', lookup_expr='lte')

    class Meta:
        model = Invoice
        fields = '__all__'
        exclude = ['place', 'date_created', 'total', 'customer_name', 'no_of_products']
