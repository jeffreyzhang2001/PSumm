from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import UnsummarizedTextForm
from .test import uppercase

# Create your views here.
def index(request):
    return render(request, 'index.html', {'form': UnsummarizedTextForm()})

def summarize(request):
    original_text = request.GET.get('unsummarized_text')
    nice = uppercase(original_text)
    args = {'summarized_text': original_text, 'ok' :nice}

    return render(request, 'summary.html', args)
