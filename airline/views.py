import uuid 

from django.http import JsonResponse, HttpRequest
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from aircraft.models import Aircraft

from .models import Airline
from .serializers import AirlineSerializer


### First chain
def airline_list(request: HttpRequest):
    airlines = Airline.objects.all()
    serializer = AirlineSerializer(airlines, many=True)
    return JsonResponse(serializer.data, status=200, safe=False)

def airline_create(request: HttpRequest):
    data = {
        'name': request.data.get('name'),
        'callsign': request.data.get('callsign'),
        'founded_year': request.data.get('founded_year'),
        'base_airport': request.data.get('base_airport')
    }

    serializer = AirlineSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    
    return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def chain_list_post(request: HttpRequest):
    if request.method == 'GET':
        return airline_list(request)
    if request.method == 'POST':
        return airline_create(request)
    
### Second chain.
def airline_get(request: HttpRequest, pk=str):
    try:
        airline = Airline.objects.get(pk=pk)
    except Airline.DoesNotExist:
        return JsonResponse({'error': 'Airline not found'}, status=404)
    serializer = AirlineSerializer(airline)
    return JsonResponse(serializer.data, status=200)

def airline_patch(request: HttpRequest, pk=str):
    
    data = dict()
    airline_attr_names = ['name', 'callsign', 'founded_year', 'base_airport']
    for attr in airline_attr_names:
        temp = request.data.get(attr, None)
        if temp != None:
            data[attr] = temp

    try:
        airline = Airline.objects.get(pk=pk)
    except Airline.DoesNotExist:
        return JsonResponse({'error': 'Airline not found'}, status=404)
    
    serializer = AirlineSerializer(airline, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    
    return JsonResponse(serializer.errors, status=405)

def airline_delete(request: HttpRequest, pk: str):
    try:
        airline = Airline.objects.get(pk=pk)
    except Airline.DoesNotExist:
        return JsonResponse({'error': 'Airline not found.'}, status=404)
    
    airline.delete()
    return JsonResponse({'message': 'Airline deleted.'}, status=204)

@api_view(['GET', 'PATCH', 'POST'])
@permission_classes([IsAuthenticated])
def chain_get_patch_delete(request: HttpRequest, pk: str):
    if request.method == 'GET':
        return airline_get(request=request, pk=pk)
    if request.method == 'PATCH':
        return airline_patch(request=request, pk=pk)
    if request.method == 'POST':
        return airline_delete(request=request, pk=pk)

### Single aircraft delete method.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def aircraft_delete(request: HttpRequest, pk: uuid.UUID):
    try:
        aircraft = Aircraft.objects.get(pk=pk)
    except Aircraft.DoesNotExist:
        return JsonResponse({'error': 'Aircraft not found.'}, status=404)
    
    aircraft.delete()
    return JsonResponse({'message': 'Aircraft deleted.'}, status=204)
