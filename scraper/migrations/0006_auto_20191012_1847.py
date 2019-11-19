# Generated by Django 2.2.6 on 2019-10-12 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0005_auto_20191012_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='dietary',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='glutenFree',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='hasEggs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='hasFish',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='hasMilk',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='hasPeanuts',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='hasShellfish',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='hasSoy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='hasTreenuts',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='hasWheat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='isVegan',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='isVegetarian',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='menu',
            name='meal',
            field=models.CharField(choices=[('Continental', 'Continental'), ('Breakfast', 'Breakfast'), ('Brunch', 'Brunch'), ('Lunch', 'Lunch'), ('Late Lunch', 'Late Lunch'), ('Midday', 'Midday'), ('Dinner', 'Dinner'), ('Lite Dinner', 'Lite Dinner'), ('Late Night', 'Late Night')], max_length=50),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
