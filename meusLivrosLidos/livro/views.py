from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.db.models import Q
from .models import Livro
from .forms import LivroForm


class LivroListView(ListView):

    model = Livro
    template_name = 'livro/livro_list.html'
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).order_by('-inicio')


class LivroAboutView(TemplateView):
    template_name = 'livro/livro_about.html'

    def get_context_data(self, *args, **kwargs):
        context = super(LivroAboutView, self).get_context_data(**kwargs)        
        context['livro'] = Livro.objects.get(pk=kwargs.get('pk', None))
        return context


class LivroCreate(CreateView):
    model = Livro
    template_name = 'livro/livro_edit.html'
    form_class = LivroForm

    def form_valid(self, form):        
        livro = form.save(commit=False)
        livro.user = self.request.user        
        return super(LivroCreate, self).form_valid(form)


class LivroUpdate(UpdateView):
    model = Livro    
    template_name = 'livro/livro_edit.html'
    form_class = LivroForm


class LivroDelete(DeleteView):
    model = Livro
    template_name = 'livro/confirm_delete.html'
    success_url = reverse_lazy('livro:livro-list')