# Generated by Django 3.2.13 on 2022-09-26 22:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=10000)),
                ('name', models.CharField(max_length=1000)),
                ('description', models.TextField(max_length=1000000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('based', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.list')),
                ('host', models.ManyToManyField(to='base.movieimg')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
