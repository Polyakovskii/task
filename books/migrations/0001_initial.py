# Generated by Django 3.0.5 on 2020-07-15 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
