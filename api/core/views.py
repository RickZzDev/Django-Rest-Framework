from django.shortcuts import render
from .models import Empresas
from .serializers import EmpresaSerializer

from rest_framework import status,viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Metodo que lista todos
# @api_view(['POST', 'PUT','GET'])
# def api_detail_empresa_view(request):

#     # if request.method == 'GET':
#     #     empresa = Empresas.objects.all()

#     if request.method == 'POST':
#         serializer = EmpresaSerializer(data = request.data)
#         if serializer.is_valid():
#             # return Response(serializer.data['nome'])
#             serializer.save()
#             return Response(serializer.data)
#     else:
#         serializer = EmpresaSerializer(data=request.data)
#         if serializer.is_valid():
#             return Response({'entrou nou put':serializer.data})
  






# Create your views here.
class EmpresaViewSet(viewsets.ModelViewSet):
        queryset = Empresas.objects.all()
        serializer_class = EmpresaSerializer
            

#

    