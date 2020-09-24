from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import NDC
# Create your views here.

def home_page_view(request):
    return HttpResponse('你好!')


class NDCListView(ListView):
    model = NDC
    template_name = 'NDC_list.html'
