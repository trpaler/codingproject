from django.shortcuts import render
from .models import *
from datetime import datetime, date
from django.template import defaultfilters
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
	context = {}
	return render(request, 'weatherapp/index.html', context)