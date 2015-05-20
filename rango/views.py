from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

def index(request):
    # # return HttpResponse("Rango says hey there world!")
    # # Construct a dictionary to pas to the templae engine as its context.
    # context_dict = {'boldmessage' : "I am bold font from the context"}

    # # this goes to templates/rango/index.html
    # return render(request, 'rango/index.html', context_dict)


    # Query the database for a list of ALL categories currently stored
    # Order the categories by no. likes in descending order
    # Retrieve the top 5 only 
    # Place the list in our context_dict dictionary which will be passed to the template engine
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories' : category_list}

    return render(request, 'rango/index.html', context_dict)

def about(request):
	return HttpResponse("In the about section")

def category(request, category_name_slug):
	context_dict = {}

	try:
		category = Category.objects.get(slug=category_name_slug)
		context_dict['category_name'] = category.name

		# this is a filter that retrieves all the associated pages of a specific category
		pages = Page.objects.filter(category=category)

		context_dict['pages'] = pages

		context_dict['category'] = category 
	except Category.DoesNotExist:
		pass

	return render(request, 'rango/category.html', context_dict)
