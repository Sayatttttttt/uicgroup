# Generated by Django 5.0.4 on 2024-05-05 09:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Filial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filial', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('second_name', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('father', models.CharField(max_length=200)),
                ('status', models.CharField(default='Pending', max_length=200)),
                ('mass', models.IntegerField(default=None)),
                ('volume', models.IntegerField(default=None)),
                ('filial_receive', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='filial_receive', to='post.filial')),
                ('filial_send', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filial_send', to='post.filial')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=200)),
                ('filial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.filial')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
