from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    output = '''
    <html>
        <head>
            first view
        </head>
        <body>
            first view
        </body>
    </html>
    '''
    
    return HttpResponse(output)