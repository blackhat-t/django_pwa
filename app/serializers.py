from rest_framework  import serializers
from .models import Mpesa

class MpesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mpesa
        fields = ('created_on', 'amount', 'phone_number', 'token')