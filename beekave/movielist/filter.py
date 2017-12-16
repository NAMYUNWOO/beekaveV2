from detail.models import Movie
import django_filters

class MovieFilter(django_filters.FilterSet):
    class Meta:
        model = Movie
        fields = ['openyear']