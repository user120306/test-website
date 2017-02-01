from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer
# Create your views here.

#list all stocks or creates a new one
class StockList(APIView):
	def get(sel, request):
		stock = Stock.objects.all()
		serializer = StockSerializer(stock, many=True)
		return Response(serializer.data)

	def post(self):
		pass