from rest_framework.generics import ListAPIView
from .serializers import ProductSerializer
from .models import Product
from django_filters.rest_framework import DjangoFilterBackend
# search filters
from rest_framework.filters import SearchFilter
# pagination
from rest_framework.pagination import LimitOffsetPagination

# create class of productpagination
class ProductsPagination(LimitOffsetPagination):
    # set default limit
    default_limit = 3
    # set maximum limit
    max_limit = 5

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', )
    # search fields
    search_fields = ('name', 'description')
    # add pagination class
    pagination_class = ProductsPagination

    # Knowing about django-filters which helps to search by query like /products/?id=3 shows data of product with id 3
    def get_queryset(self):
        on_sale = self.request.query_params.get('on_sale', None)
        if on_sale == None:
            return super().get_queryset()
        queryset = Product.objects.all()
        
        if on_sale.lower() == 'true':
            from django.utils import timezone
            now = timezone.now()
            return queryset.filter(
                sale_start__lte=now,
                sale_end__gte=now
            )
        return queryset