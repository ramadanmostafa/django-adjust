from django_filters import FilterSet, DateFilter, CharFilter

from metrics.models import DataSet


class DataSetFilter(FilterSet):
    date_gte = DateFilter(lookup_expr='gte', field_name='date')
    date_lte = DateFilter(lookup_expr='lte', field_name='date')
    channel = CharFilter(lookup_expr='icontains')
    country = CharFilter(lookup_expr='icontains')
    os = CharFilter(lookup_expr='icontains')

    class Meta:
        model = DataSet
        fields = ('date', 'channel', 'country', 'os')
