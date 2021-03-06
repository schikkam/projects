# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from myproject.storage.models import (
    Document
)

from myproject.storage.forms import (
    DocumentForm
)

def service(request):

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            userid = form.cleaned_data['userid']
            token = form.cleaned_data['token']

            newdoc = Document(docfile=request.FILES['docfile'],
                              userid=userid, token=token)
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('service'))
    else:
        form = DocumentForm()  # A empty, unbound form

    return render(
        request,
        'service.html',
        {'form': form}
    )

"""
def upload(request):
    # Handle file upload
    import pdb
    pdb.set_trace()

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            userid = form.cleaned_data['userid']
            token = form.cleaned_data['token']

            newdoc = Document(docfile=request.FILES['docfile'],
                              userid=userid, token=token)
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = UploadForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'upload.html',
        {'documents': documents, 'form': form}
    )

def list(request):
    # list files
    form = DocumentForm()  # A empty, unbound form
    documents = Document.objects.all()

    return render(
        request,
        'list.html',
        {'documents': documents, 'form': form}
    )
"""