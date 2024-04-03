from django.shortcuts import render

finches = [
  {'name': 'Lolo', 'breed': 'finchy', 'description': 'feathery little demon', 'age': 3},
  {'name': 'Sachi', 'breed': 'finchless', 'description': 'gentle and loving', 'age': 2},
]

# Create your views here.

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'about.html')

# Add new view
def finches_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'finches/index.html', {
    'finches': finches
  })
