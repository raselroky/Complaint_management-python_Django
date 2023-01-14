from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import Complainant_InfoSerializer

class Complainant_Info_View(APIView):
    def post(self,request):
        serializer=Complainant_InfoSerializer
        if(serializer.is_valid()):
            serializer.save()
            return Response({"Message":"Complainant_Info recieve Succesfully"})
        return Response({"Message":"Errors"})
