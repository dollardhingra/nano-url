from urlshortner.models import Url
from django.http.response import Http404
from django.shortcuts import render, HttpResponseRedirect


def index(request):
    url_obj = None
    if request.method == "POST":
        original_name = request.POST["original_name"]
        try:
            url_obj = Url.objects.get(original_name=original_name)
        except Url.DoesNotExist:
            url_obj = Url(original_name=original_name)   
            url_obj.save()
        
    return render(request, "urlshortner/index.html", {
        "url_obj": url_obj,
        "base_url": request.build_absolute_uri('/')
    })

def redirect(request, short_name):
    try:
        url = Url.objects.get(short_name=short_name)
    except Url.DoesNotExist:
        raise Http404("Url does not exist")

    url.count_open += 1        
    url.save()
    return HttpResponseRedirect(url.original_name)