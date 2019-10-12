from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class Menu(models.Model):
    location = models.charField(max_length=50)
    meal = models.charField(max_length=50)
    date = models.DateField()
    menuItems = models.ManyToManyField(MenuItem)

class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    #station = models.CharField(max_length=50)
    DIETARY_CHOICES = [
        ('prop-vegetarian', 1),
        ('prop-vegan', 2),
        ('prop-made_without_gluten', 3),
        ('allergen-has_egg', 4),
        ('allergen-has_soy', 5),
        ('allergen-has_wheat', 6),
        ('allergen-has_milk', 7),
        ('allergen-has_fish', 8),
        ('allergen-has_shellfish', 9),
        ('allergen-has_peanut', 10),
        ('allergen-has_tree_nuts', 11)
    ]
    dietary = MultiSelectField(choices=DIETARY_CHOICES)
