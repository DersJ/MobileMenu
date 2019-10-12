from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=50, unique=True)
    #station = models.CharField(max_length=50)
    """DIETARY_CHOICES = [
        ('prop-vegetarian', 'vegetarian'),
        ('prop-vegan', 'vegan'),
        ('prop-made_without_gluten', 'gluten free'),
        ('allergen-has_egg', 'has eggs'),
        ('allergen-has_soy', 'has soy'),
        ('allergen-has_wheat', 'has wheat'),
        ('allergen-has_milk', 'has milk'),
        ('allergen-has_fish', 'has fish'),
        ('allergen-has_shellfish', 'has shellfish'),
        ('allergen-has_peanut', 'has peanuts'),
        ('allergen-has_tree_nuts', 'has tree nuts')
    ]
    dietary = MultiSelectField(choices=DIETARY_CHOICES)"""
    isVegetarian = models.BooleanField(default = False)
    isVegan = models.BooleanField(default = False)
    glutenFree = models.BooleanField(default = False)
    hasEggs = models.BooleanField(default = False)
    hasSoy = models.BooleanField(default = False)
    hasWheat = models.BooleanField(default = False)
    hasMilk = models.BooleanField(default = False)
    hasFish = models.BooleanField(default = False)
    hasShellfish = models.BooleanField(default = False)
    hasPeanuts = models.BooleanField(default = False)
    hasTreenuts = models.BooleanField(default = False)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Menu(models.Model):
    MEALS = [
        ('Continental', 'Continental'),
        ('Breakfast', 'Breakfast'),
        ('Brunch', 'Brunch'),
        ('Lunch', 'Lunch'),
        ('Late Lunch', 'Late Lunch'),
        ('Midday', 'Midday'),
        ('Dinner', 'Dinner'),
        ('Lite Dinner', 'Lite Dinner'),
        ('Late Night', 'Late Night'),
    ]
    meal = models.CharField(max_length=50, choices=MEALS)
    date = models.DateField()
    menuItems = models.ManyToManyField(MenuItem)
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return location + ' ' + date
