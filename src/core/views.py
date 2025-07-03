from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, FileResponse, HttpResponseBadRequest
from django.core.paginator import Paginator

from epub2go.convert import get_all_books, Book, allbooks_url

import os
from urllib.parse import urlparse
import logging

from epub2go_web.tasks import getEpub

logger = logging.getLogger(__name__) #TODO configure logging

books = sorted(get_all_books(), key= lambda b: b.title)# TODO get from pickle
books_count = len(books)
logger.info('Found %s books', books_count)
gbnetloc = urlparse(allbooks_url).netloc

def index(request: HttpRequest):
    localbooks = books

    targetParam = request.GET.get('t', None)
    searchParam = request.GET.get('s', None)
    if targetParam:
        if validateUrl(targetParam):
            # download file
            result = getEpub.delay(targetParam)
            fpath = result.get(timeout=60)
            fname = os.path.basename(fpath)
            file = open(fpath, 'rb')
            response = FileResponse(file)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = f'attachment; filename="{fname}"'
            return response
        else: return HttpResponseBadRequest('Input URL invalid.')
    elif searchParam:
        search = searchParam.lower()
        localbooks = [book for book in books if search in book.title.lower() or search in book.author.lower()]

    # paginate items
    paginationParam = request.GET.get('p', '')
    try:
        pageNo = int(paginationParam)
    except ValueError:
        pageNo = 1

    pages = Paginator(localbooks, 100)
    if pageNo < 1 or pageNo > pages.num_pages:
        pageNo = 1
    page = pages.page(pageNo)
    context = {
        'title': 'epub2go',
        'http_host': f'http://{ request.META['HTTP_HOST'] }',
        'page': page,
        'allbooks_count': books_count,
        'allbooks_url': allbooks_url,
    }
    # return base view
    return render(request, 'home.html', context)

def validateUrl(param)->bool :

    netloc = urlparse(param).netloc
    if(netloc == gbnetloc): return True

    return False
