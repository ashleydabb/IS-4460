from django.shortcuts import render
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework import generics

class CustomerListCreateView(generics.ListCreateAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerListCreateView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer





# Create your views here.
