from rest_framework.routers import DefaultRouter
from api.views import BlogModelView
from django.urls import path, include

router = DefaultRouter()
router.register(r'blogs', BlogModelView)

urlpatterns = [
    path('', include(router.urls)),
]
