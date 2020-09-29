from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, NDCViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', NDCViewSet, basename='ndcs')

urlpatterns = router.urls
