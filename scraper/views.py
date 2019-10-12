from django.shortcuts import render, redirect
from .scraper import getItems

# Create your views here.
def scraperview(request):
    getItems("https://dining.unc.edu/locations/chase/", "chase")
    return redirect('/')
