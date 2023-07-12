from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Women, Category
from .serializers import WomenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework.decorators import action


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

    @action(methods=["get"], detail=False)
    def category(self, request):
        cats = Category.objects.all()
        return Response({"cats": [c.name for c in cats]})

    

