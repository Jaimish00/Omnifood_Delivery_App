# Generated by Django 3.1 on 2020-09-12 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0001_initial'),
        ('food', '0002_food_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='hotel',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='food', to='custom_user.hoteladmin'),
        ),
    ]
