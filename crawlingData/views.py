from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
# Create your views here.
def main_page(request):
    template = get_template('main_page.html')
    variables = Context({
        'head_title' : 'Odd Comparison',
        'body' : 'Do make odd comparison service for korean proto'
    })
    
    output = template.render(variables)
    return HttpResponse(output)
