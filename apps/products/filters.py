from django_filters import FilterSet, ModelChoiceFilter, DateFilter

from apps.products.models import Product, PriceInterval


class PriceStatsFilter(FilterSet):
    product = ModelChoiceFilter(queryset=Product.objects.all())
    start_date = DateFilter(field_name='start_date', lookup_expr='gte')
    end_date = DateFilter(field_name='end_date', lookup_expr='lte')

    class Meta:
        model = PriceInterval
        fields = ('product', 'start_date', 'end_date')