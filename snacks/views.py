from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Snack
from django.urls import reverse_lazy

class Snacks(ListView):
    template_name='Home.html'
    model= Snack

class SnackList(DetailView):
    template_name='snack_detail.html'
    model= Snack

class Create(CreateView):
    template_name='create.html'
    model=Snack
    fields=['title','purchaser','discreption']
class Update(UpdateView):
    template_name='update.html'
    model=Snack
    fields=['title','purchaser','discreption']
class Delete(DeleteView):
    template_name='delete.html'
    model=Snack
    success_url=reverse_lazy('snack')
    
