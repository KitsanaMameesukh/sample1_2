# Generated by Django 4.0.2 on 2022-05-02 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoLists',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=255)),
                ('todo', models.TextField(max_length=500)),
                ('startDate', models.TextField(max_length=10)),
                ('endDate', models.TextField(max_length=10)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
