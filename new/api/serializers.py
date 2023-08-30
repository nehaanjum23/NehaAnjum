from rest_framework import serializers
from .models import student

class studentSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
    class Meta:
        model=student
        fields=['name','roll','city']

class studentGetSerializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'