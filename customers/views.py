from customers.models import Customer
from django.http import JsonResponse
from customers.serializers import CustomersSerializer

def customers(request):
   data = Customer.objects.all()  #invoke serializer and return to client
   serializer = CustomersSerializer(data, many=True)
   return JsonResponse({'customers': serializer.data})