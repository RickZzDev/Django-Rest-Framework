from django.urls import path
from core import views

urlpatterns = [
    path('empresas/', views.snippet_list),
    path('empresas/<int:pk>/', views.snippet_detail),
]