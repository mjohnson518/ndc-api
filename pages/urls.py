from django.urls import path, include
from . import views
from .views import home_page_view, SignupPageView, AboutPageView, NDCListView, NDCDetailView, LicensePageView


urlpatterns = [
    path('', home_page_view.as_view(), name='home'),
    path('NDCs/', NDCListView.as_view(), name='NDC_list'),
    path('NDC/<slug:slug>/', NDCDetailView.as_view(), name='NDC_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('data-license/', LicensePageView.as_view(), name='license'),
]
