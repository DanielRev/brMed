
import requests 
import datetime
from pandas.tseries.offsets import BDay


class Currency:
	def __init__(self):
		self.symbols = self.getCurrencySymbols()
		#Dictionary of dates to rates for currencies
		self.rates = {} 
		self.ratesLast5Days()
		#print("TESTE LEN:", len(self.rates))
		#print(self.rates)

	def getCurrencySymbols(self):
		url = "https://api.vatcomply.com/currencies"
		return requests.get(url).json()


	#d parameter is a date object
	def getRatesForDate(self, d):
		url = "https://api.vatcomply.com/rates?base=USD&date=" + str(d.date())
		rates_for_d = requests.get(url).json()
		#TODO(?): cortar fora todos exceto os que usarei.
		self.rates[rates_for_d['date']] = rates_for_d['rates']


	#Recupera ultimos 5 dias uteis
	#TODO: conferir se esta usando feriados BR
	def getLast5BuisnessDays(self):
		today = datetime.datetime.today()
		buisness_days = []
		for n in range(6):
			#print(n)
			buisness_days.append(today - BDay(n))
		return buisness_days
	
	def ratesLast5Days(self):
		b_days = self.getLast5BuisnessDays()
		for day in b_days:
			self.getRatesForDate(day)


#----------------------------------------------------------------------------------------
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