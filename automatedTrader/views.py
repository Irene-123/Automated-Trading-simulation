from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import csv, io 
from table import Table

def index(request): 
    return  render(request, 'index.html') 

def ohlc(request): 
    csv_fp = open(f'static/ohlc.csv', 'r')
    reader = csv.DictReader(csv_fp)
    headers = [col for col in reader.fieldnames]
    out = [row for row in reader]
    return render(request, 'ohlc.html', {'data' : out, 'headers' : headers})
   
    



