import urllib.request
from bs4 import BeautifulSoup
from .models import *

def getItems(url, loc):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    bigDiv = soup.find("div", {'id': 'menu-tabs'})
    allitems = bigDiv.find_all("a", {"class": 'show-nutrition'})

    class Item:
        def __init__(self, tag):
            self.name = tag.string
            self.classes = tag['class']


    #items = []
    #for item in allitems:
    item = allitems[0]
    veget = item['class'].find('prop-vegetarian')
    vegan = item['class'].find('prop-vegan')
    gluten = item['class'].find('prop-made_without_gluten')
    eggs = item['class'].find('allergen-has_egg')
    soy = item['class'].find('allergen-has_soy')
    wheat = item['class'].find('allergen-has_wheat')
    milk = item['class'].find('allergen-has_milk')
    fish = item['class'].find('allergen-has_fish')
    shellfish = item['class'].find('allergen-has_shellfish')
    peanut = item['class'].find('allergen-has_peanut')
    treenuts = item['class'].find('allergen-has_tree_nuts')
    a = MenuItem(name=item.string,
        isVegetarian = veget,
        isVegan = vegan,
        glutenFree = gluten,
        hasEggs = eggs,
        hasSoy = soy,
        hasWheat = wheat,
        hasMilk = milk,
        hasFish = fish,
        hasShellfish = shellfish,
        hasPeanuts = peanut,
        hasTreenuts = treenuts)
    a.save()
        #items.append(Item(item))
    #return items

def getMenu(url, loc):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    bigDiv = soup.find("div", {'id': 'menu-tabs'})
    ctabsnav = soup.find("div", {'class': 'c-tabs-nav'})
    mealtimes = ctabsnav.find_all("a")
    indivMeal = bigDiv.find_all("div", {"class": 'c-tab'})

    class Meal:
        def __init__(self, location, time, itemlist):
            self.location = location
            self.time = time
            self.itemlist = itemlist

    menu = []
    for meal in mealtimes:
        mealmenu = indivMeal[int(meal['data-tabid'])].find_all("a")
        time = meal.find("div").string.split("(")[0].rstrip()
        menu.append(Meal(loc, time, mealmenu))
    return menu

chase = "https://dining.unc.edu/locations/chase/"
lenoir = "https://dining.unc.edu/locations/top-of-lenoir/"

getMenu(chase, "Chase")
#getMenu(pageL, "Lenoir")
