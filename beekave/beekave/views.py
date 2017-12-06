from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from beekave.forms import UserCreationForm


class UserCreateView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'register_done.html'


def search(request,myfilter):
    context = {"searchResult":myfilter}
    return render(request,"searchResult.html",context)