from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from . import currency

def index(request):
	template = loader.get_template('currencyApp/index.html')
	context = currency.Currency().rates
	#return HttpResponse(template.render(context, request))
	#return render(request, 'currencyApp/index.html', context)
	return render(request, 'currencyApp/index.html', {'rates': context})


#Temporario, remover
import requests 
from datetime import date
def teste(request):
	c = currency.Currency()
	# print(c.teste())
	d = date(2002, 12, 31)
	c.getRatesForDate(d)
	#print(c.rates)
	return HttpResponse(c.rates)

def teste2(request):
    url = "https://api.vatcomply.com/rates?base=USD&date=2020-04-05"        
    return HttpResponse(requests.get(url).content)