from .models import Log
import django_filters
from django import forms
from django_filters.widgets import RangeWidget

class LogFilter(django_filters.FilterSet):

    sourceip = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    time = django_filters.TimeRangeFilter(
        widget=RangeWidget(attrs={'type': 'time'})
    )

    dns_a_record_query = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Log
        fields = ['sourceip', 'time', 'dns_a_record_query']