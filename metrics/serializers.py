from collections import OrderedDict

from rest_framework import serializers

from metrics.models import DataSet


def set_dynamic_fields(serializer, fields=None, exclude=None):
    if not (fields or exclude) or not hasattr(serializer, 'fields'):
        return
    if exclude is None:
        exclude = []
    if fields is None:
        fields = set(serializer.fields.keys())
    existing = set(serializer.fields.keys())
    excluded = set(exclude).intersection(existing)  # Drop any fields that are not specified in the `fields` argument.

    # Drop any fields that are not specified in the `fields` argument.
    nested_fields = OrderedDict()
    for field in fields:
        parts = field.split('.', 1)
        main_field = parts[0]
        if main_field not in nested_fields:
            nested_fields[main_field] = []
        nested_fields[main_field].extend(parts[1:])
    allowed = set(nested_fields.keys())

    to_be_excluded = (existing - allowed).union(excluded)

    for field_name in to_be_excluded:
        serializer.fields.pop(field_name)

    for nested_field, specific_fields in nested_fields.items():
        if not specific_fields or nested_field not in serializer.fields:
            continue
        set_dynamic_fields(serializer.fields[nested_field], specific_fields)


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)
        super().__init__(*args, **kwargs)
        self.set_fields(fields, exclude)

    def set_fields(self, fields, exclude):
        set_dynamic_fields(self, fields, exclude)


class MetricsSerializer(DynamicFieldsModelSerializer):
    cost_per_install = serializers.DecimalField(max_digits=50, decimal_places=2)
    class Meta:
        model = DataSet
        fields = (
            "id",
            "date",
            "channel",
            "country",
            "os",
            "impressions",
            "clicks",
            "installs",
            "spend",
            "revenue",
            "cost_per_install"
        )
