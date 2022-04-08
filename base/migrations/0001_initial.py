# Generated by Django 4.0.3 on 2022-04-08 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('species', models.CharField(max_length=20)),
                ('weight', models.IntegerField()),
                ('length', models.IntegerField()),
                ('latitude', models.DecimalField(decimal_places=3, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=3, max_digits=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
