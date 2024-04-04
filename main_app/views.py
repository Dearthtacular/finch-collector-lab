from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch

# Create your views here.

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'about.html')

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'
  
class FinchUpdate(UpdateView):
  model = Finch
  # Let's disallow the renaming of a finch by excluding the name field!
  fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'


# Add new view
def finches_index(request):
  finches = Finch.objects.all()
  # We pass data to a template very much like we did in Express!
  return render(request, 'finches/index.html', {
    'finches': finches
  })

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', { 'finch': finch })
