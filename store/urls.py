from django.urls import path
from .api_views import *

urlpatterns = [
    path('v1/products/', ProductList.as_view()),
]
