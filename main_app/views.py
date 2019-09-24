from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import Items
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class ItemCreate(CreateView):
    model = Items
    fields = ['name']
    success_url = '/'

    

class ItemDelete(DeleteView):
    model = Items
    success_url = '/'

def home(request):
  item_list = Items.objects.all()
  return render(request, 'home.html', { 'item_list': item_list })


