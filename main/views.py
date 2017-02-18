from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
from main.tools.dateconverter import NepaliDateConverter
def index(request):
    converter = NepaliDateConverter()
    year = datetime.date.today().year
    month = datetime.date.today().month
    day = datetime.date.today().day

    date = converter.ad2bs((year,month,day))
    return HttpResponse(converter.format_date(date,target="np"))
