from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from .models import NDC
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm


class SignupPageView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'

class home_page_view(TemplateView):
    template_name = 'index.html'


class NDCListView(ListView):
    model = NDC
    template_name = 'pages/NDC_list.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class NDCDetailView(DetailView):
    model = NDC
    template_name = 'pages/NDC_detail.html'
