from django.urls import path,include
from .views import ClientViewset, ProjectViewset,ProjectUserViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('client',ClientViewset)
router.register('project',ProjectViewset)
router.register('user',ProjectUserViewset)

urlpatterns = [
    path('', include(router.urls)),
]