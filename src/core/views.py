from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from epub2go.convert import get_all_books, Book

def index(request: HttpRequest):
    title = 'epub2go'
    targetParam = request.GET.get('t', None)
    books = get_all_books()
    if targetParam is not None:
        getEpub(targetParam)
    return render(request, 'index.html', locals())

def getEpub(param):
    print(param)
    # TODO validate / sanitize input
    # TODO check for existing file and age
    # TODO download
    # TODO redirect to loading page
    # TODO redirect to download page
    raise NotImplementedError
