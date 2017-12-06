from django.shortcuts import render
from django.core.urlresolvers import resolve


# Create your views here.
def aboutus(request):
    current_url = resolve(request.path_info).url_name
    context = {}
    if current_url == "contactus":
        context["contents"] = "contactus"
    elif current_url == "faq":
        context["contents"] = "faq"
    else:
        context["contents"] = "aboutus"
    return render(request,'aboutus.html',context)