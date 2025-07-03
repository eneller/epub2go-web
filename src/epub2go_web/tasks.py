from celery import shared_task
from django.conf import settings

from epub2go.convert import GBConvert

converter = GBConvert(downloaddir=settings.MEDIA_ROOT)

@shared_task
def getEpub(book_url):
    # TODO check for existing file and age
    return converter.download(book_url)

def getDir(book_url):
    return converter.getDir(book_url)
