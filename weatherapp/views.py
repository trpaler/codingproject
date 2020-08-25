import json
from django.shortcuts import render

from django.template import RequestContext
from django.http import HttpResponse
from django.urls import reverse

from weatherapp.models import Document
from weatherapp.forms import DocumentForm

def index(request):
    # Handle file upload
    context = {}
    lines = []
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            docfile = request.FILES['docfile']
            for line in docfile:
                lines.append(str(line))

            newdoc = Document(docfile=docfile, date=request.POST.get('date'))
            newdoc.save()
            context['lines'] = str(lines)
            context['status'] = 200
            context['date'] = newdoc.date

    else:
        form = DocumentForm()

    # Load documents for the index page
    context['form'] = form
    # Render index page with the documents and the form
    return render(request, 'weatherapp/index.html', context)