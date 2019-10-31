from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from app.models import FornecedorIndividual
from app.forms import InsereFornecedorForm
def index(request):
    context = {}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context, request))


def gentella_html(request):
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/' + load_template)
    return HttpResponse(template.render(context, request))

class FornecedorIndividualListView(ListView):
    template_name = "gentelella/form.html"
    model = FornecedorIndividual
    context_object_name = "fornecedores"

class FornecedorIndividualCreateView(CreateView):
    template_name = "gentelella/form.html"
    model = FornecedorIndividual
    form_class = InsereFornecedorForm

class FornecedorIndividualUpdateView(UpdateView):
    template_name = "gentelella/form.html"
    model = FornecedorIndividual
    fields = '__all__'
    context_object_name = 'fornecedor'

class FornecedorIndividualDeleteView(DeleteView):
    template_name = "gentelella/form.html"
    model = FornecedorIndividual
    context_object_name = 'fornecedor'
