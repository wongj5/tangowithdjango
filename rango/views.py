from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Rango says hey there world!")
    # Construct a dictionary to pas to the templae engine as its context.
    context_dict = {'boldmessage' : "I am bold font from the context"}

    # this goes to templates/rango/index.html
    return render(request, 'rango/index.html', context_dict)

def about(request):
	return HttpResponse("In the about section")
