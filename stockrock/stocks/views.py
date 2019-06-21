from django.shortcuts import render,redirect
from .forms import StockSearchForm
import json
from .models import Stock
import pandas as pd
import requests

def search_stock(request):
    form = StockSearchForm(request.POST or None)
    if form.is_valid():
        stock_name = form.cleaned_data['name']
        try:
            s = Stock.objects.get(name=stock_name)
            function = 'TIME_SERIES_DAILY_ADJUSTED'
            ticker = f'NSE:{s.ticker}'
            outputsize =  'compact'
            apikey = 'IWLKTDPIS9TEFIFF'

            url = f'https://www.alphavantage.co/query?function={function}&symbol={ticker}&outputsize={outputsize}&apikey={apikey}&datatype=csv'
            df = pd.read_csv(url)
            df = df.drop(['open','high','low','close','volume','dividend_amount','split_coefficient'],axis=1)

            print(df.head())
            stock_data = df.to_json(orient='columns')
            stock_data_final = json.dumps(stock_data)
            return render(request,'stocks/stockView.html',{"stock_name":stock_name,'stock_data':stock_data_final})

        except:
            print("There was some error") 
            return render(request,'stocks/notfound.html')          
    return render(request,'stocks/search.html',{'form':form, 'title':'Search Stock'})
