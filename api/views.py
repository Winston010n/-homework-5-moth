from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view 

class Hello(APIView):
    def get(self, request):
        return Response({
            "message": "APiView in restframework like this" 
        } ) 
        
@api_view(['GET']) 
def hello_api(request):
    return Response({
            "message": "Hello from API view"
        } ) 
    
class People(APIView):
    def get(self, request):
        return Response({
            'name': 'alisher',
            'city': 'osh',
            'year': 2000,
            'geo': 'geeks'
        } ) 
        
@api_view(['GET'])
def people_api(request):
    return Response({
            'name': 'alisher',
            'city': 'osh',
            'year': 2000,
            'geo': 'geeks'
        } ) 