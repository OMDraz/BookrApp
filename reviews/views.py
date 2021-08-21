"""
# Explanation for each of the imports and helpful definitions
    HttpResponse: This is a method that handles what we respond to the server
    QueryDict: Objects that mostly behave like dictionaries, except with multiple values for a key.
    Render: A shortcut function that returns an HttpResponse. It takes two args (request, template)
"""
from django.http import HttpResponse
from .models import Book
from django.shortcuts import render


"""
This is a function that returns a response to the client saying Hello World.
1. We get the name attribute from the url - and we parse it into the HttpResponse using the format function
2. To pass variables from views to templates, we need to pass it explicitly in the context  
"""

def index(request):
    name = request.GET.get('name') or "World!"
    return render(request, 'base.html', context={
        'name': name,
    })

def search(request, query):
    return render(request, 'base.html', context={
        'query': query,
    })

def welcome_view(request):
    message = f'<html><h1>Welcome to Bookr!</h1><p>{Book.objects.count()} books and counting!</p></html>'
    return HttpResponse(message)