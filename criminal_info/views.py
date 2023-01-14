from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Criminal_InfoSerializer

class Criminal_Info_View(APIView):
    def post(self,request):
        serializer=Criminal_InfoSerializer
        if(serializer.is_valid()):
            serializer.save()
            return Response({"Message":"criminal_info data recieve Successfully"})
        return Response({"Message":"Errors"})
