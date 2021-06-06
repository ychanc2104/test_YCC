from .models import Log
import django_filters
from django import forms
from django_filters.widgets import RangeWidget

class LogFilter(django_filters.FilterSet):

    sourceip = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    date = django_filters.DateRangeFilter(
        widget=RangeWidget(attrs={'type': 'date'})
    )
    time = django_filters.TimeRangeFilter(
        widget=RangeWidget(attrs={'type': 'time'})
    )
    usec = django_filters.RangeFilter(
        widget=RangeWidget()
    )
    dns_a_record_query = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Log
        fields = ['sourceip', 'dns_a_record_query','datetime', 'date', 'time', 'usec']