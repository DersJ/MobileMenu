from django.shortcuts import render, redirect
from .scraper import *

# Create your views here.
def scraperview(request):
    lenoir = "https://dining.unc.edu/locations/top-of-lenoir/"
    chase = "https://dining.unc.edu/locations/chase/"
    #getMenu(chase, "Chase")
    return redirect('/')
