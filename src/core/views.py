from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, FileResponse
from django.conf import settings

from epub2go.convert import get_all_books, Book, GBConvert

import os

converter = GBConvert(downloaddir=settings.MEDIA_ROOT)

def index(request: HttpRequest):
    title = 'epub2go'
    targetParam = request.GET.get('t', None)
    books = get_all_books()
    if targetParam:
        epub = getEpub(targetParam)
        fname = os.path.join(settings.MEDIA_ROOT, epub)
        file =  open(fname, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(fname)}"'
        return response

    return render(request, 'index.html', locals())

def getEpub(param):
    print(param)
    # TODO validate / sanitize input
    # TODO check for existing file and age
    #GBConvert(param,downloaddir=settings.MEDIA_ROOT).run()
    # TODO redirect to loading page
    # TODO redirect to download page
    raise NotImplementedError
