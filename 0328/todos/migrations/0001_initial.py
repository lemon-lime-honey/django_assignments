# Generated by Django 3.2.18 on 2023-03-28 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=80)),
                ('completed', models.BooleanField(default=False)),
                ('priority', models.IntegerField(default=3)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('deadline', models.DateField(null=True)),
            ],
        ),
    ]
