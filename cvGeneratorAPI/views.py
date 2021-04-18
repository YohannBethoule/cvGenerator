from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from cvGeneratorBO.models import *
from cvGeneratorBO.serializers import SiteSerializer

# Create your views here.

@api_view(['GET'])
def data_site(request, urlName):
    # GET data for site
    try:
        data = Site.objects.filter(published=True).get(urlName=urlName)
    except Site.DoesNotExist:
        return JsonResponse({'message': 'The site does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data_serializer = SiteSerializer(data, context={'request': request})
        return JsonResponse(data_serializer.data)
