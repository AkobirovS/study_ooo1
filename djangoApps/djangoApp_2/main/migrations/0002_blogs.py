# Generated by Django 5.1.6 on 2025-02-14 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('context', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
