from rest_framework import generics
from .Serializer import FoodSerializer
from .models import Food


class MenuListView(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class MenuDetailView(generics.DestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class MenuCreateView(generics.CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
