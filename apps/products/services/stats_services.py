from datetime import datetime

from django.db.models import Avg
from rest_framework.response import Response


class StatsCalculate:
    def __init__(self, queryset, request):
        self.queryset = queryset
        self.request = request

    def calculate(self):
        response = {'price': self.queryset.aggregate(Avg('price')).get('price__avg')}
        if self.request.query_params.get('end_date') and self.request.query_params.get('start_date'):
            end_date = datetime.strptime(self.request.query_params.get('end_date'), '%Y-%m-%d')
            start_date = datetime.strptime(self.request.query_params.get('start_date'), '%Y-%m-%d')
            days = end_date - start_date
            response['days'] = days.days + 1
        return Response(response, status=200)
