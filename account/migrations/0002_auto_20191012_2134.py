# Generated by Django 2.2.6 on 2019-10-12 21:34

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0004_auto_20191012_1600'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='locations',
            field=models.ManyToManyField(to='scraper.Location'),
        ),
        migrations.AddField(
            model_name='user',
            name='meals',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Continental'), (2, 'Breakfast'), (3, 'Brunch'), (4, 'Lunch'), (5, 'Late Lunch'), (6, 'Midday'), (7, 'Dinner'), (8, 'Lite Dinner'), (9, 'Late Night')], default='', max_length=17),
        ),
    ]