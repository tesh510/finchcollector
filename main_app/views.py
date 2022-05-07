from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Add the Cat class & list and view function below the imports
class Finch:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

finches = [
  Finch('Alex', 'tabby', 'little demon', 3),
  Finch('EJ', 'tortoise shell', 'diluted tortoise shell', 0),
  Finch('Maroof', 'black tripod', '1 legged finch', 4)
]

def home(request):
  return HttpResponse('<h1> Birdiesssssss <Oo/V\oO> </h1>')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', { 'finches': finches })