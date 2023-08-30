from django.shortcuts import render
from .models import student
from .serializers import studentSerializer,studentGetSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class studentView(APIView):
    def post(self,request):
        serializer=studentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'created successfully'},status=status.HTTP_201_CREATED)
        else:
            return Response({'msg':'Invaild'},status=status.HTTP_400_BAD_REQUEST)

class studentGetView(APIView):
    def get(self,request):
        stu=student.objects.all()
        serializer=studentGetSerializer(stu,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
class studentUpdate(APIView):
    def put(self,request,id):
        stu=student.objects.get(id=id)
        serializer=studentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'updated successfully'},status=status.HTTP_200_OK)
        else:
            return Response({'msg':'Invalid'},status=status.HTTP_400_BAD_REQUEST)

class studentDeleteView(APIView):
    def delete(self,request,id):
        stu=student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Deleted Successfully'},status=status.HTTP_200_OK)