# Generated by Django 2.1.2 on 2019-01-28 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rooms', models.CharField(choices=[('studio', 'Студия'), ('1', '1-комнатная квартира'), ('2', '2-комнатная квартира'), ('3', '3-комнатная квартира'), ('4', '4-комнатная квартира'), ('5', '5-комнатная квартира'), ('6', '6-комнатная квартира')], max_length=10, verbose_name='Rooms')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('area', models.IntegerField(verbose_name='Area')),
                ('balcony_type', models.CharField(choices=[('1b', 'Балкон'), ('1l', 'Лоджия'), ('1b1l', 'Балкон и лоджия')], max_length=10, verbose_name='Rooms')),
                ('mortgage', models.BooleanField(verbose_name='Mortgage')),
                ('army_mortgage', models.BooleanField(verbose_name='Army Mortgage')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartments', to='common.City', verbose_name='City')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
