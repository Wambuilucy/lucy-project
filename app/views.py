from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from .serializers import ImageSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import *

@csrf_exempt
def tutorials_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ImageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def image_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        images = Image.objects.get(pk=pk)
    except Image.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ImageSerializer(images)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ImageSerializer(images, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        images.delete()
        return HttpResponse(status=204)


