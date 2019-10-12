from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    #station = models.CharField(max_length=50)
    DIETARY_CHOICES = [
        (1, 'prop-vegetarian'),
        (2, 'prop-vegan'),
        (3, 'prop-made_without_gluten'),
        (4, 'allergen-has_egg'),
        (5, 'allergen-has_soy'),
        (6, 'allergen-has_wheat'),
        (7, 'allergen-has_milk'),
        (8, 'allergen-has_fish'),
        (9, 'allergen-has_shellfish'),
        (10, 'allergen-has_peanut'),
        (11, 'allergen-has_tree_nuts')
    ]
    dietary = MultiSelectField(choices=DIETARY_CHOICES)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Menu(models.Model):
    MEALS = [
        (1, 'Continental'),
        (2, 'Breakfast'),
        (3, 'Brunch'),
        (4, 'Lunch'),
        (5, 'Late Lunch'),
        (6, 'Midday'),
        (7, 'Dinner'),
        (8, 'Lite Dinner'),
        (9, 'Late Night'),
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
