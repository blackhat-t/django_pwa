from django.shortcuts import render
from rest_framework import  generics
from  .models import Mpesa
from django.views import  generic
from .serializers import MpesaSerializer

class MpesaList(generics.ListCreateAPIView):
    queryset = Mpesa.objects.order_by('-created_on').all()
    template_name = 'index.html'
    serializer_class = MpesaSerializer


class MpesaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mpesa.objects.all()
    serializer_class = MpesaSerializer
    def post(self, request, *args, **kwargs):
        data = request.data
        send_message(data['phone_number'],data['code'])

class MpesaLisst(generic.ListView):
    queryset = Mpesa.objects.order_by('-created_on').all()
    template_name = 'index.html'
    serializer_class = MpesaSerializer


