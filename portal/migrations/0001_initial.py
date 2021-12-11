# Generated by Django 3.1.6 on 2021-12-07 05:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите категорию заявки', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Portal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('решена', 'Решена'), ('отклонена', 'Отклонена'), ('новая', 'Новая')], default='Новая', max_length=10)),
                ('photo', models.ImageField(null=True, upload_to='images/')),
                ('categories', models.ManyToManyField(help_text='Укажите категорию заявки', to='portal.Categories')),
            ],
        ),
    ]