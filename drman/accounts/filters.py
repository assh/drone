import django_filters
from .models import *

class MissionFilter(django_filters.FilterSet):
    class Meta:
        model=Mission
        fields='__all__'