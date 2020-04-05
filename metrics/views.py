from django.db.models import Sum, F, ExpressionWrapper, DecimalField
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from metrics.filters import DataSetFilter
from metrics.models import DataSet
from metrics.serializers import MetricsSerializer


class ListMetrics(ListAPIView):
    serializer_class = MetricsSerializer
    filter_class = DataSetFilter
    queryset = DataSet.objects.all()
    filter_backends = (DjangoFilterBackend, )
    SORT_BY_CHOICES = (
        'date', 'channel', 'country', 'os', 'impressions', 'clicks', 'spend', 'revenue', 'cost_per_install'
    )
    ORDER_CHOICES = ('asc', 'desc')
    DEFAULT_ORDERING = 'date'

    def get_fields(self):
        fields = self.request.GET.get('fields')
        if fields:
            return fields.split(',')

    def get_ordering(self):
        sort_by = self.request.GET.get('sort_by', 'date')
        order = self.request.GET.get('order', 'asc')
        if order not in self.ORDER_CHOICES or sort_by not in self.SORT_BY_CHOICES:
            return self.DEFAULT_ORDERING
        ordering = '-' if order == 'desc' else ''
        ordering += sort_by
        return ordering

    def group_by(self, queryset):
        group_by = self.request.GET.get('group_by')
        fields = self.get_fields()
        if not fields or not group_by:
            return queryset
        group_by = group_by.split(',')
        fields_annotate = list(set(self.get_fields()) - set(group_by))
        annotation_options = {}
        for field in fields_annotate:
            annotation_options[field] = Sum(field)
        return queryset.values(*group_by).annotate(**annotation_options).values(*fields)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().annotate(
            cost_per_install=ExpressionWrapper(
                expression=F('spend') / F('installs'), output_field=DecimalField(max_digits=5, decimal_places=2)
            )
        ))
        queryset = queryset.order_by(self.get_ordering())
        queryset = self.group_by(queryset)
        fields = self.get_fields()
        serializer = self.get_serializer(queryset, many=True, fields=fields)
        return Response(serializer.data)
