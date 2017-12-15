from django.shortcuts import render

# Create your views here.
def movielist(request,range,scoretype):
    context ={
        "range":range,
        "scoretype":scoretype
    }
    return render(request,"movielist.html",context)
