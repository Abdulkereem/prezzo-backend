from rest_framework import serializers
from .models import Blog

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title','subtitle','banner','uuid']




class SinglePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title','subtitle','banner','article','author']
