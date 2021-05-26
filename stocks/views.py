from django.shortcuts import render
from nsetools import Nse
from stocks.models import TopGainer, TopLoser


def get_stocks():

    try:
        TopGainer.objects.all().delete()
    except Exception:
        pass

    try:
        TopLoser.objects.all().delete()
    except Exception:
        pass

    gainers = []
    for gainer in Nse().get_top_gainers():
        data = {
            'company': gainer['symbol'],
            'high': gainer['highPrice'],
            'low': gainer['lowPrice'],
            'last': gainer['ltp'],
            'prev': gainer['previousPrice']
        }
        gainers.append(data)
        TopGainer(company=data['company'], high=data['high'], low=data['low'], last=data['last'], prev=data['prev']).save()

    losers = []

    for loser in Nse().get_top_losers():
        data = {
            'company': loser['symbol'],
            'high': loser['highPrice'],
            'low': loser['lowPrice'],
            'last': loser['ltp'],
            'prev': loser['previousPrice']
        }
        losers.append(data)
        TopLoser(company=data['company'], high=data['high'], low=data['low'], last=data['last'], prev=data['prev']).save()

    return gainers, losers


# Create your views here.
def index(request):
    top_gainers, top_losers = get_stocks()
    return render(request, 'stocks.html', {'top_gainers': top_gainers, 'top_losers': top_losers})
