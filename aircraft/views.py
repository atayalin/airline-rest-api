from django.http import JsonResponse, HttpRequest
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from .models import Aircraft
from .serializers import AircraftSerializer


### First chain
def aircraft_list(request: HttpRequest):
    aircrafts = Aircraft.objects.all()
    aircrafts = list(aircrafts.values())
    serializer = AircraftSerializer(aircrafts, many=True)
    return JsonResponse(serializer.data, status=200)

def aircraft_create(request: HttpRequest):
    data = {
        'manufacturer_serial_number': request.data.get('manufacturer_serial_number'),
        'type': request.data.get('type'),
        'model': request.data.get('model'),
        'operator_airline': request.data.get('operator_airline'),
        'number_of_engines': request.data.get('number_of_engines')
    }

    serializer = AircraftSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    
    return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def chain_list_post(request: HttpRequest):
    if request.method == 'GET':
        return aircraft_list(request=request)
    if request.method == 'POST':
        return aircraft_create(request=request)

### Second chain
def aircraft_get(request: HttpRequest, pk=str):
    try:
        aircraft = Aircraft.objects.get(pk=pk)
    except Aircraft.DoesNotExist:
        return JsonResponse({'error': 'Aircraft not found'}, status=404)
    serializer = AircraftSerializer(aircraft)
    return JsonResponse(serializer.data, status=200)

def aircraft_patch(request: HttpRequest, aircraft_id=str):
    
    data = dict()
    aircraft_attr_names = ['manufacturer_serial_number', 'type', 'model', 'operator_airline', 'number_of_engines']
    for attr in aircraft_attr_names:
        temp = request.data.get(attr, None)
        if temp != None:
            data[attr] = temp

    try:
        aircraft = Aircraft.objects.get(pk=aircraft_id)
    except Aircraft.DoesNotExist:
        return JsonResponse({'error': 'Aircraft not found'}, status=404)
    
    serializer = AircraftSerializer(aircraft, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, 200)
    
    return JsonResponse(serializer.errors, status=405)

@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def chain_get_patch_delete(request: HttpRequest, pk: int):
    if request.method == 'GET':
        return aircraft_get(request=request, pk=pk)
    if request.method == 'PATCH':
        return aircraft_patch(request=request, pk=pk)