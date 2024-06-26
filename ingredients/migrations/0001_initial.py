# Generated by Django 5.0.3 on 2024-03-28 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipes', '0002_alter_recipes_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('recipe', models.ManyToManyField(related_name='ingredients', to='recipes.recipes')),
            ],
        ),
    ]
