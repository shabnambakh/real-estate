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
            name='MailTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('body', models.TextField(verbose_name='Body')),
            ],
        ),
        migrations.CreateModel(
            name='MailType',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Code')),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribers', to='common.City', verbose_name='City')),
            ],
        ),
        migrations.AddField(
            model_name='mailtemplate',
            name='mail_type',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='subscriber.MailType', verbose_name='Mail Type'),
        ),
    ]
