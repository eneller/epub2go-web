from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, FileResponse, HttpResponseBadRequest
from django.conf import settings
from celery import shared_task

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
        'http_host': request.META['HTTP_HOST'],
        'books': books,
        'book_count': len(books),
    }

    targetParam = request.GET.get('t', None)
    if targetParam:
        if validateUrl(targetParam):
            # download file
            fpath = getEpub(targetParam)
            fname = os.path.basename(fpath)
            file = open(fpath, 'rb')
            response = FileResponse(file)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = f'attachment; filename="{fname}"'
            return response
        else: return HttpResponseBadRequest('Input URL invalid.')
    else:
        # return base view
        return render(request, 'index.html', context)

def validateUrl(param)->bool :

    netloc = urlparse(param).netloc
    if(netloc == gbnetloc): return True

    return False

# TODO make this async and show some indication of progress/loading
#@shared_task
def getEpub(book_url):
    # TODO check for existing file and age
    return converter.download(book_url)
