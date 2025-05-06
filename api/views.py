from rest_framework.viewsets import ModelViewSet
from api.models import Category, Tag, BlogPost
from api.serializers import BlogSerializer


class BlogModelView(ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer
