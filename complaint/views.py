from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ComplaintSerializer
from .models import Complaint

class ComplaintView(APIView):
    def post(self,request):
        serializer=ComplaintSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({"Message":"Successfully Done!"})
        return Response({"Message":"Errors"})
