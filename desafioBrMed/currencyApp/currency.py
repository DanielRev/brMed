
import requests 
from datetime import date



class Currency:
	def __init__(self):
		self.symbols = self.getCurrencySymbols()
		#Dictionary of dates to rates for currencies
		self.rates = {} 


	def getCurrencySymbols(self):
		url = "https://api.vatcomply.com/currencies"
		return requests.get(url).content


	#d parameter is a date object
	def getRatesForDate(self, d):
		url = "https://api.vatcomply.com/rates?base=USD&date=" + str(d)
		rates_for_d = requests.get(url).json()
		#teste
		#print(rates_for_d['rates']['EUR'])
		#possibilidade: cortar fora todos exceto os que usarei.
		self.rates[rates_for_d['date']] = rates_for_d['rates']



	#testes remover
	def teste(self):
	    url = "https://api.vatcomply.com/rates?base=USD"
	    json_response = requests.get(url).json()
	    return json_response
	    # t1 = requests.get(url)
	    # print(type(t1.json()))
	    # return requests.get(url).content

	def teste2(self):
	    url = "https://api.vatcomply.com/rates?base=USD&date=2020-04-05"        
	    return requests.get(url).content