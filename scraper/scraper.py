import urllib.request
import datetime
from bs4 import BeautifulSoup
from .models import *

def getItems(url):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    bigDiv = soup.find("div", {'id': 'menu-tabs'})
    allitems = bigDiv.find_all("a", {"class": 'show-nutrition'})

    for item in allitems:
        if len(MenuItem.objects.filter(name = item.string)) == 0:
            a = MenuItem.objects.create(name = item.string,
                isVegetarian = 'prop-vegetarian' in item['class'],
                isVegan = 'prop-vegan' in item['class'],
                glutenFree = 'prop-made_without_gluten' in item['class'],
                hasEggs = 'allergen-has_egg' in item['class'],
                hasSoy = 'allergen-has_soy' in item['class'],
                hasWheat = 'allergen-has_wheat' in item['class'],
                hasMilk = 'allergen-has_milk' in item['class'],
                hasFish = 'allergen-has_fish' in item['class'],
                hasShellfish = 'allergen-has_shellfish' in item['class'],
                hasPeanuts =  'allergen-has_peanut' in item['class'],
                hasTreenuts = 'allergen-has_tree_nuts' in item['class'])

def getMenu(url, loc):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    bigDiv = soup.find("div", {'id': 'menu-tabs'})
    ctabsnav = soup.find("div", {'class': 'c-tabs-nav'})
    mealtimes = ctabsnav.find_all("a")
    indivMeal = bigDiv.find_all("div", {"class": 'c-tab'})
    meal_iter = 0

    for meal in mealtimes:
        a = Menu.objects.create(
            meal = meal.find("div").string.split("(")[0].rstrip(),
            date = datetime.date.today(),
            location = Location.objects.filter(name = loc)[0]
        )
        this_meal_items = indivMeal[meal_iter].find_all("a", {"class": "show-nutrition"})
        for item in this_meal_items:
            item_object = MenuItem.objects.filter(name = item.string)[0]
            a.menuItems.add(item_object)

        a.save()
        meal_iter += 1
