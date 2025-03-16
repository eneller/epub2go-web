from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, FileResponse
from django.conf import settings

from epub2go.convert import get_all_books, Book, GBConvert, allbooks_url

import os
from urllib.parse import urlparse
import logging

logger = logging.getLogger(__name__) #TODO configure logging

converter = GBConvert(downloaddir=settings.MEDIA_ROOT)
books = get_all_books()# TODO get from pickle
gbnetloc = urlparse(allbooks_url).netloc

def index(request: HttpRequest):
    context = {
        'title': 'epub2go',
        'books': books,
    }

    targetParam = request.GET.get('t', None)
    if validateUrl(targetParam):
        epub = getEpub(targetParam)
        fname = os.path.join(settings.MEDIA_ROOT, epub)
        file =  open(fname, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(fname)}"'
        return response

    return render(request, 'index.html', context)

def validateUrl(param)->bool :
    if not param: return False

    netloc = urlparse(param).netloc
    if(netloc == gbnetloc): return True

    return False

def getEpub(param):
    # TODO validate / sanitize input
    # TODO check for existing file and age
    #GBConvert(param,downloaddir=settings.MEDIA_ROOT).run()
    # TODO redirect to loading page
    # TODO redirect to download page
    raise NotImplementedError
