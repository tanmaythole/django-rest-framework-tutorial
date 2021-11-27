from rest_framework.generics import ListAPIView
from .serializers import ProductSerializer
from .models import Product
from django_filters.rest_framework import DjangoFilterBackend

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('id', )

    # Knowing about django-filters which helps to search by query like /products/?id=3 shows data of product with id 3
    def get_queryset(self):
        on_sale = self.request.query_params.get('on_sale', None)
        if on_sale == None:
            return super.get_queryset()
        queryset = Product.objects.all()
        
        if on_sale.lower() == 'true':
            from django.utils import timezone
            now = timezone.now()
            return queryset.filter(
                sale_start__lte=now,
                sale_end__gte=now
            )
        return queryset