from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView, ListView, DetailView, View
from .models import NDC
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django_downloadview import ObjectDownloadView


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

class LicensePageView(TemplateView):
    template_name = 'pages/data-license.html'

class NDCDetailView(DetailView):
    model = NDC
    template_name = 'pages/NDC_detail.html'

class FileDownloadView(View):
    # Set FILE_STORAGE_PATH value in settings.py
    folder_path = settings.MEDIA_ROOT
    # Here set the name of the file with extension
    file_name = "{{ ndc.NDC_Text }}"
    # Set the content type value
    content_type_value = 'PDF'

    def get(self, request, file_name):
        self.file_name = file_name
        file_path = os.path.join(self.folder_path, self.file_name)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(
                    fh.read(),
                    content_type=self.content_type_value
                )
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
        else:
            raise Http404
