from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import BrandSerializers, ProductSerializers, CategorySerializers
from .models import Product, Category, Brand
from django.shortcuts import get_object_or_404


class CategoryView(viewsets.ViewSet):

    queryset = Category.objects.all()
    def list(self, request):
        serializer = CategorySerializers(self.queryset, many=True)
        return Response(serializer.data)
    def retrive(self, request, pk):
        queryset = Category.objects.all()
        cate = get_object_or_404(queryset, id=pk)
        serializer = CategorySerializers(cate, many=False)
        return Response(serializer.data)
