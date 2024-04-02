from .models import Drink
from django.http import JsonResponse
from .serializers import DrinkSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view(['GET'])
def drink_list(request):
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return Response(serializer.data)
