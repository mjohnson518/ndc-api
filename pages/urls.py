from django.urls import path
from .views import home_page_view, NDCListView

urlpatterns = [
    path('', home_page_view, name='home'),
    path('NDCs/', NDCListView.as_view(), name='NDC_list'),
]
