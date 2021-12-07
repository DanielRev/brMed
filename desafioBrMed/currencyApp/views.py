# from django.shortcuts import render
# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

from django.http import HttpResponse
from django.template import loader
from . import currency

def index(request):
    template = loader.get_template('currencyApp/index.html')
    context = {
        'latest_question_list': 1,
    }
    return HttpResponse(template.render(context, request))


import requests 
from datetime import date

#Temporario, remover
def teste(request):
	c = currency.Currency()
	# print(c.teste())
	d = date(2002, 12, 31)
	c.getRatesForDate(d)
	print(c.rates)
	return HttpResponse(c.rates)

def teste2(request):
    url = "https://api.vatcomply.com/rates?base=USD&date=2020-04-05"        
    return HttpResponse(requests.get(url).content)