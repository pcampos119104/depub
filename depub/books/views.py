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
