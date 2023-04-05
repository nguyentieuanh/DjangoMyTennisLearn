from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.
#Xử lý các request của người dùng và trả về respoonse
def member(request): 
    # response = HttpResponse()
    # response.writelines("<h1> Hello World</h1>")
    # response.write("This is my app")
    mymembers = Member.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {
        'mymembers': mymembers
    }
    return HttpResponse(template.render(context, request))

def details(request, id): 
    mymember = Member.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        "mymember": mymember, 
    }
    return HttpResponse(template.render(context, request))

def main(request): 
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def testing(request): 
    template = loader.get_template('testing.html')
    # fruits = ['Apple', 'Banana', 'Orange']
    context = {
        'greeting': 0, 
    }
    return HttpResponse(template.render(context, request))