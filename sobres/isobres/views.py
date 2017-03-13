from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render, render_to_response


# Create your views here.
def homepage(request):
    return render_to_response("homepage.html",
    {
        'title': 'iCorrupt',
        'context': 'A envelope manager',
        'author' : 'Luis Barcenas',
        'username' : 'Rajoy'
    })
    #page = template.render(variables)
    #return HttpResponse(page)

def dashboard(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404('User not found, asshole!')

    sobres = user.sobre_set.all()

    template = get_template('dashboard.html')
    variables = Context({
        'username': username,
        'sobres': sobres
    })
    page = template.render(variables)
    return HttpResponse(page)
