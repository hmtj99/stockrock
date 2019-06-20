from django.shortcuts import render

def search_stock(request):
    return render(request,"stocks/search.html")

    

