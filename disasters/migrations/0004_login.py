# Generated by Django 5.0.6 on 2024-09-15 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disasters', '0003_delete_heading'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=122)),
            ],
        ),
    ]
