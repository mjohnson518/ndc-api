from django.urls import path
from .views import home_page_view, SignupPageView, AboutPageView, NDCListView

urlpatterns = [
    path('', home_page_view.as_view(), name='home'),
    path('NDCs/', NDCListView.as_view(), name='NDC_list'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('signup/', SignupPageView.as_view(), name='signup')
]
