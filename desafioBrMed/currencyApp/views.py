# from django.shortcuts import render
# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

from django.http import HttpResponse
from django.template import loader
import requests 

def index(request):
    template = loader.get_template('currencyApp/index.html')
    context = {
        'latest_question_list': 1,
    }
    return HttpResponse(template.render(context, request))


#Temporario, remover
def teste(request):
    url = "https://api.vatcomply.com/rates?base=USD"
    return HttpResponse(requests.get(url).content)

def teste2(request):
    url = "https://api.vatcomply.com/rates?base=USD&date=2020-04-05"        
    return HttpResponse(requests.get(url).content)