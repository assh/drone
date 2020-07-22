import django_filters
from .models import *
from django_filters import DateFilter


class MissionFilter(django_filters.FilterSet):
    #start_date = django_filters.DateTimeFromToRangeFilter(widget=django_filters.widgets.RangeWidget(
    #    attrs={'class': 'datepicker'}
    #))
    start_date = DateFilter(field_name="date_future",lookup_expr='lte')

    class Meta:
        model = Mission
        fields = '__all__'
        exclude = ['customer', 'date_future','mission_pic']
