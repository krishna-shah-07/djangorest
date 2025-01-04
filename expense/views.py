from django.shortcuts import render

# Create your views here.

from .models import Transaction
from rest_framework.response import Response
from .serializers import TransactionSerializer
from rest_framework.decorators import api_view

#decorator to specify the type of request and modify function behavior
@api_view()
def get_transactions(request):
    queryset = Transaction.objects.all()
    serializer = TransactionSerializer(queryset, many=True)
    return Response({"data" : serializer.data})