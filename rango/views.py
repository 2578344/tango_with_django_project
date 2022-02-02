from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponse
#Import the category model
from rango.models import Category
from rango.models import Page

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    return render(request, 'rango/index.html', context = context_dict)

def about(request):

    context_dict = {'boldmessage2' : 'here is the about page.','boldmessage': 'This tutorial has been put together by MICHAL GOLABEK'}
   # return HttpResponse("Rango says here is the about page" + "<a href='/rango'>  Get back</a>")
    return render(request, 'rango/about.html', context = context_dict)

def show_category(request, category_name_slug):
    """Our new view follows the same basic steps as our index() view. We first define a
context dictionary. Then, we attempt to extract the data from the models and add
the relevant data to the context dictionary. We determine which category has been
requested by using the value passed category_name_slug to the show_category() view
function (in addition to the request parameter).
If the category slug is found in the Category model, we can then pull out the associated
pages, and add this to the context dictionary, context_dict. If the category
requested was not found, we set the associated context dictionary values to None.
Finally, we render() everything together, using a new category.html template.
    """
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['category'] = None

    return render(request, 'rango/category.html', context=context_dict)
