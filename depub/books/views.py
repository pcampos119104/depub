from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
class Create(View):
    template = 'books/create_update.html'

    def get(self, request):
        # epub_file_form = EpubFileForm()
        context = {
            'text': 'Create and Update page',
        }
        return render(request, self.template, context)

    def post(self, request):
        pass

def process_epub(request):
    """
    Process the epub to extract the metadata and return the form.
    """
    import time
    time.sleep(2.5)
    return
