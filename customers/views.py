from customers.models import Customer
from django.http import JsonResponse, Http404
from customers.serializers import CustomersSerializer

def customers(request):
   data = Customer.objects.all()  #invoke serializer and return to client
   serializer = CustomersSerializer(data, many=True)
   return JsonResponse({'customers': serializer.data})


def customer(request, id):
   try:
      data = Customer.objects.get(pk=id)  #invoke serializer and return to client
   except Customer.DoesNotExist:
      raise Http404('Customer does not exist')
   serializer = CustomersSerializer(data)
   return JsonResponse({'customer': serializer.data})