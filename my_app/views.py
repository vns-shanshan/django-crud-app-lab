from django.shortcuts import render
from django.http import HttpResponse
from .models import Dog

# class Dog:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age

# dogs = [
#     Dog('Coconut', 'Beagle', 'It looks like a small foxhound.', 3),
#     Dog('Milky', 'Bulldog', 'Stocky dog that moves with a rolling gait.', 0),
#     Dog('Fancy', 'Poodle', 'Extremely intelligent and are easily trained.', 4),
#     Dog('Aires', 'Yorkshire', 'Long hair.', 6)
# ]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dog_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {"dogs": dogs})

def dog_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dogs/detail.html', {"dog": dog})