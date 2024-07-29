from django.shortcuts import render
from django.db.models import Prefetch

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import FoodListSerializer
from .models import FoodCategory, Food


@api_view(['GET'])
def get_food(request):
    food = FoodCategory.objects.prefetch_related(Prefetch(
    'food', queryset=Food.objects.filter(is_publish=True))).filter(food__is_publish=True).distinct().order_by('order_id')
    serializer = FoodListSerializer(food, many=True)
    return Response(serializer.data)

