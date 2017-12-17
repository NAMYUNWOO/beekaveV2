from detail.models import Movie
import django_filters

class MovieFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Movie
        fields = ['openyear','title','genre']