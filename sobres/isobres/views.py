from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    page = """
    <html>
    <body>
    Bribes management application
    (c) Luis Barcenas, 2017
    </body>
    </html>
    """
    return HttpResponse(page)
