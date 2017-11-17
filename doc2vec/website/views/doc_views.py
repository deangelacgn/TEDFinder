from .modules import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.detail import SingleObjectMixin

from website.forms import DocumentForm

class DocumentList(ListView):
    model = Document
    context_object_name = "documents"
    template_name = "website/docs/docs.html"
    paginate_by = 10
    page_kwarg = 'pagina'
    ordering = ['title', 'date']
    doc_form = DocumentForm

    def get_context_data(self, **kwargs):
        context = super(DocumentList, self).get_context_data(**kwargs)
        context['doc_form'] = self.doc_form
        context['doc_error'] = self.request.session.pop('doc_error', None)
        print(context)
        return context

@method_decorator(login_required, name='dispatch')
class DocumentView(View):
    def get(self, request, *args, **kwargs):
        view = DocumentList.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            doc = form.save()
        else:
            request.session['doc_error'] = form.errors

        print(request.POST)
        print(request.FILES)
        print(form.errors)

        return redirect('doc_view')


@method_decorator(login_required, name='dispatch')
class DocumentDelete(DeleteView):
    model = Document
    success_url = reverse_lazy('doc_view')
    template_name = "website/docs/docs.html"
