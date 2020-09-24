from django.shortcuts import render
from django.views.generic import TemplateView
import yfinance as yf
import lxml
from github import Github
import requests as r
import json

stocks =[]
tsla = yf.Ticker("TSLA")
tsla_data = tsla.info
dayHigh = tsla_data['dayHigh']
dayLow = tsla_data['dayLow']
longName = tsla_data['longName']
twoHundredDayAverage = tsla_data['twoHundredDayAverage']
stocks.append(tuple([longName, dayHigh, dayLow, twoHundredDayAverage]))

msft = yf.Ticker("MSFT")
msft_data = msft.info
dayHigh = msft_data['dayHigh']
dayLow = msft_data['dayLow']
longName = msft_data['longName']
twoHundredDayAverage = msft_data['twoHundredDayAverage']
stocks.append(tuple([longName, dayHigh, dayLow, twoHundredDayAverage]))

aapl = yf.Ticker("AAPL")
aapl_data = aapl.info
dayHigh = aapl_data['dayHigh']
dayLow = aapl_data['dayLow']
longName = aapl_data['longName']
twoHundredDayAverage = aapl_data['twoHundredDayAverage']
stocks.append(tuple([longName, dayHigh, dayLow, twoHundredDayAverage]))

goog = yf.Ticker("GOOG")
goog_data = goog.info
dayHigh = goog_data['dayHigh']
dayLow = goog_data['dayLow']
longName = goog_data['longName']
twoHundredDayAverage = goog_data['twoHundredDayAverage']
stocks.append(tuple([longName, dayHigh, dayLow, twoHundredDayAverage]))

#token deleted in this file
g = Github("token_here")
repos = g.get_user().get_repos(visibility='public')

fact_data = r.get("https://cat-fact.herokuapp.com/facts")
fact = fact_data.json()['all'][:1]
fact_text = fact[0]['text']

class APIPage(TemplateView):
    """docstring for APIPage."""
    template_name = 'myapis/apis.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['stocks'] = stocks
        context['repos'] = repos
        context['fact_text'] = fact_text
        return context

