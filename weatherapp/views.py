from django.shortcuts import render

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse

from weatherapp.models import Document
from weatherapp.forms import DocumentForm

def index(request):
    # Handle file upload
    context = {}
    if request.method == 'POST':
        print(request.POST)
        print('asdasdasdasdasd')
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            docfile = request.FILES['docfile']
            for line in docfile:
                print(line)
            newdoc = Document(docfile=docfile, date=request.POST.get('date'))
            newdoc.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)
    else:
        form = DocumentForm()

    # Load documents for the index page
    documents = Document.objects.all()
    context = {'documents': documents, 'form': form}

    # Render index page with the documents and the form
    return render(request, 'weatherapp/index.html', context)