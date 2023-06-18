# Generated by Django 4.1.7 on 2023-06-15 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_managers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Managers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('telefon', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='managers.category_managers')),
            ],
        ),
    ]