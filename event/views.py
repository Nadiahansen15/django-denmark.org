from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.views.generic import ListView
from .models import Event

# Create your views here.
class LandingpageView(ListView):
    model = Event
    template_name = "event/landingpage.html"
    ordering = ['date']