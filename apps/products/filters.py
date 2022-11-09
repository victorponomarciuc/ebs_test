from django.db.models import Q
from django_filters import FilterSet, ModelChoiceFilter, DateFilter

from apps.products.models import Product, PriceInterval


class PriceStatsFilter(FilterSet):
    product = ModelChoiceFilter(queryset=Product.objects.all())
    start_date = DateFilter(method="get_start_date")
    end_date = DateFilter(method="get_end_date")

    class Meta:
        model = PriceInterval
        fields = ('product', 'start_date', 'end_date')

    def get_start_date(self, qs, name, values):
        return qs.filter(Q(start_date__lte=values) | Q(end_date__gte=values))

    def get_end_date(self, qs, name, values):
        return qs.filter(Q(end_date__gte=values) | Q(start_date__lte=values))
