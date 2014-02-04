from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
# Create your views here.
def main_page(request):
    template = loader.get_template('main_page.html')
    context = RequestContext(request, {
        'head_title' : 'Odd Comparison',
        'body_word' : 'Do make odd comparison service for korean proto',
    })
    output = template.render(context)
    return HttpResponse(output)
