from django.shortcuts import render

# Create your views here.

from .models import Transaction
from rest_framework.response import Response
from .serializers import TransactionSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.db.models import Sum

#decorator to specify the type of request and modify function behavior
@api_view(['GET'])
def get_transactions(request):
    queryset = Transaction.objects.all()
    serializer = TransactionSerializer(queryset, many=True)
    return Response({"data" : serializer.data})

class TransactionAPI(APIView):
    #get method to fetch all the transactions from the database
    def get(self, request):
        queryset = Transaction.objects.all().order_by('-date')
        serializer = TransactionSerializer(queryset, many=True)
        return Response({
            "data" : serializer.data,
            "total" : queryset.aggregate(total=Sum('amount'))['total'] or 0
        })

    #serializer is used to validate the data and save it to the database
    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "Transaction created successfully"})
        return Response(serializer.errors)

    #pk is the primary key of the transaction to be updated or deleted
    def put(self, request, pk):
        transaction = Transaction.objects.get(id=pk)
        serializer = TransactionSerializer(instance=transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "Transaction updated successfully"})
        return Response(serializer.errors)
    
    #partial update of the transaction using patch method
    def patch(self, request, pk):
        transaction = Transaction.objects.get(id=pk)
        serializer = TransactionSerializer(instance=transaction, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "Transaction updated successfully"})
        return Response(serializer.errors)

    #delete method to delete the transaction from the database
    def delete(self, request):
        data = request.data
        if data.get('id'):
            transaction = Transaction.objects.get(id=data.get('id'))
            transaction.delete()
            return Response({"message" : "Transaction deleted successfully"})
        return Response({"message" : "Please provide the id of the transaction to delete"})