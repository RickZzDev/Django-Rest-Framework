from django.shortcuts import render, get_object_or_404
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
# A EMPRESA VIEW SET É COMO SE FOSSER UMA CONTROLLER 
# ELA IDENTIFICA QUAL A AÇÃO NECESSARIA
# CHAMA O MODEL NECESSARIO
# E O SERIALIZER PARA TRANSFORMAR ESTE RETORNO EM JSON
class EmpresaViewSet(viewsets.ModelViewSet):

        
        # ESTE METODO IRA LISTAR TODOS OS REGISTROS
        def list(self, request):
            queryset = Empresas.objects.all()
            serializer_class = EmpresaSerializer(queryset, many=True)
            return Response(serializer_class.data)
            
        # ESTE METODO IRA MOSTRAR UM UNICO REGISTO
        def retrieve(self,request, pk=None):
            queryset = Empresas.objects.all()
            empresa = get_object_or_404(queryset, pk=pk)
            serializer_class = EmpresaSerializer(empresa)
            return Response(serializer_class.data)

        def  create(self,request):
          serializer = EmpresaSerializer(data = request.data)
          if serializer.is_valid():
              serializer.save()
              return Response({ 'data':serializer.data})   
          else:
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                 
        def destroy(self, request,pk=None):
          queryset = Empresa.objects.all()
          empresa = get_object_or_404(queryset, pk=pk)
          empresa.delete()
          return Response({ 'data':serializer.data})             
