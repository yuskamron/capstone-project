from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomePage(TemplateView):
		template_name = 'index.html'  # index.html bu templates folderdagi file

class InboxPage(TemplateView):
        template_name = 'inbox.html'