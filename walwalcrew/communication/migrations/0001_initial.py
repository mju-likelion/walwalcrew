# Generated by Django 3.2.5 on 2021-07-28 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='question_list',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('cateogry', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=5000)),
                ('answer', models.CharField(max_length=5)),
            ],
        ),
    ]
