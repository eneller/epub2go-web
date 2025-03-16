from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from epub2go.convert import get_all_books, Book, allbooks_url

import pickle, os

class Command(BaseCommand):
    help = "Download the Book List"

    filepath = os.path.join(settings.MEDIA_ROOT, 'books.pkl')
    def handle(self, *args, **options):
        try:
            books = get_all_books()
        except:
            raise CommandError('Failed to get Book list from %s', allbooks_url)
        try:
            with open(self.filepath, 'wb') as file:
                pickle.dump(books,file)
        except:
            raise CommandError(f'Failed to save pickle file. Did you create {settings.MEDIA_ROOT} ?')