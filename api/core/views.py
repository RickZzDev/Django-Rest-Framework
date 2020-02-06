from django.shortcuts import render
from .models import Empresas
from .serializers import EmpresaSerializer
from rest_framework import status,viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.serializers import Serializer
from django.http import JsonResponse

def snippet_detail(request, pk):
    try:
        snippet = Empresas.objects.get(pk=pk)
    except Empresas.DoesNotExist:
        return Response(status=404)

    if request.method =='GET':
            serializer = EmpresaSerializer(snippet)
            return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parser(request)
        serializer = EmpresaSerializer(snippet)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = 400)      


def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Empresas.objects.all()
        serializer = EmpresaSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmpresaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# Create your views here.
# class EmpresaViewSet(viewsets.ModelViewSet):
#     queryset = Empresas.objects.all()
#     serializer_class = EmpresaSerializer

#     def list(self,request):
#         year = '123'
#         data = {"year": request.method}

#         return Response(data)

#     def delete(self,request):
#         year = '4268'
#         data = {"year": serializer_class}
#         queryset = Empresas.objects.all()
#         serializer_class = EmpresaSerializer
#         return Response(data)

    