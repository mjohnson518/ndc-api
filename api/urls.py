from django.urls import path
from .views import NDCAPIView

urlpatterns = [
    path('', NDCAPIView.as_view()),
]
