import django_filters
from .models import Job
class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Job
        fields = ['title','category', 'experince', 'job_type', 'location', 'salary']