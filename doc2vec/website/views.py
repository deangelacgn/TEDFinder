from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404, HttpResponseForbidden
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, ModelFormMixin, CreateView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.detail import SingleObjectMixin

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'website/index.html', context)




def page_not_found(request):
    response = render_to_response(
        '404.html',
        context_instance=RequestContext(request)
    )

    response.status_code = 404
    return render(request, '404.html')
