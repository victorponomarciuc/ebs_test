from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from drf_util.views import BaseViewSet, BaseCreateModelMixin, BaseListModelMixin
from rest_framework.permissions import AllowAny

from apps.products.filters import PriceStatsFilter
from apps.products.models import Product, PriceInterval
from apps.products.serializers import ProductSerializer, PriceIntervalSerializer, ProductStatsSerializer
from apps.products.services import StatsCalculate


class ProductViewSet(BaseListModelMixin, BaseCreateModelMixin, BaseViewSet):
    permission_classes = AllowAny,
    authentication_classes = ()
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductStatsViewSet(BaseListModelMixin, BaseViewSet):
    permission_classes = AllowAny,
    authentication_classes = ()
    serializer_class = ProductStatsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PriceStatsFilter
    queryset = PriceInterval.objects.all().exclude(start_date=F('end_date'))

    def list(self, request, *args, **kwargs):
        response = StatsCalculate(queryset=self.filter_queryset(self.queryset), request=request).calculate()
        return response


class ProductPriceViewSet(BaseListModelMixin, BaseCreateModelMixin, BaseViewSet):
    permission_classes = AllowAny,
    authentication_classes = ()
    serializer_class = PriceIntervalSerializer
    queryset = PriceInterval.objects.all()

