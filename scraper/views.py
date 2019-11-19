from django.shortcuts import render, redirect
from .scraper import getItems
from .send_text import sendTexts

# Create your views here.
def scraperview(request):
    getItems("https://dining.unc.edu/locations/chase/", "chase")
    return redirect('/')

def texterview(request):
    sendTexts()
    return redirect('/')