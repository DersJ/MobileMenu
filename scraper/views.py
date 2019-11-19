from django.shortcuts import render, redirect
from .scraper import getItems
from .send_text import sendTexts

# Create your views here.
def scraperview(request):
    lenoir = "https://dining.unc.edu/locations/top-of-lenoir/"
    chase = "https://dining.unc.edu/locations/chase/"
    #getMenu(chase, "Chase")
    return redirect('/')

def texterview(request):
    sendTexts()
    return redirect('/')