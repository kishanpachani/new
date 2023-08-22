# Generated by Django 4.1 on 2023-08-21 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='image')),
                ('price', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.BigIntegerField()),
                ('product_id', models.BigIntegerField()),
                ('contity', models.BigIntegerField()),
                ('price', models.BigIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('Email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('State', models.CharField(max_length=20)),
                ('City', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=30)),
            ],
        ),
    ]
