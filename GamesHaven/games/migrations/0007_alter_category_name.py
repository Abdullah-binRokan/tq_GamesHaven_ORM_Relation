# Generated by Django 5.1.3 on 2024-11-19 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_category_alter_review_rating_game_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
