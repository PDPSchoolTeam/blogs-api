from rest_framework.serializers import ModelSerializer
from api.models import Category, Tag, BlogPost


class BlogSerializer(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = "__all__"
