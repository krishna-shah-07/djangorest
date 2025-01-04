from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        # fields = [
        #     "title",
        #     "amount",
        #     "transaction_type",
        #     "date"
        # ]

        fields = '__all__'
        
        #exclude = ['amount']