from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import UnsummarizedTextForm
from .utils import OriginalTextHandler

# Create your views here.
def index(request):
    return render(request, 'index.html', {'form': UnsummarizedTextForm()})

def summarize(request):
    original_text = request.POST.get('unsummarized_text')
    original_text_object = OriginalTextHandler(original_text)
    summarized_text = original_text_object.summarize()
    args = {'summarized_text': summarized_text}

    return render(request, 'summary.html', args)
