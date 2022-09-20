from sqlite3 import apilevel
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import json
# Create your views here.


class StudentAPIView(APIView):
    def get(self, request, format = None):

        file = open("database.json","r")
        x = file.read()
        refrence_data = json.loads(x)
        return Response(refrence_data)
       
