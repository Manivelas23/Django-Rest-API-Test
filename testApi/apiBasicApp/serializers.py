from .models import Article
from rest_framework import serializers


class articleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        #fields = ['id','title','author','email']
        fields = '__all__'

