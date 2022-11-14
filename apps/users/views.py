from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
def geeks_view(request):
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render(request))
    return render(request, "index.html")