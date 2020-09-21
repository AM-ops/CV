from django.shortcuts import render
from django.views.generic import TemplateView
import yfinance as yf
import lxml
from github import Github
import pocketcasts

tsla = yf.Ticker("TSLA")
tsla_data = tsla.info
dayHigh = tsla_data['dayHigh']
dayLow = tsla_data['dayLow']
longName = tsla_data['longName']
twoHundredDayAverage = tsla_data['twoHundredDayAverage']
g = Github("beeb76e9fc81b8c5774df15ed5632eea78234b14")
repos = g.get_user().get_repos()
pocket = pocketcasts.Pocketcasts('user@email.com',password='optional')
pocket_data = pocket.get_top_charts()[0:10]
pocket_data_clean = []
for items in pocket_data:
    title = items._title
    thumb = items._thumbnail_url
    link = items._url
    pocket_data_clean.append(tuple([title, thumb, link]))


class APIPage(TemplateView):
    """docstring for APIPage."""
    template_name = 'myapis/apis.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['longName'] = longName
        context['dayHigh'] = dayHigh
        context['dayLow'] = dayLow
        context['twoHundredDayAverage'] = twoHundredDayAverage
        context['repos'] = repos
        context['pocket_data_clean'] = pocket_data_clean
        return context
