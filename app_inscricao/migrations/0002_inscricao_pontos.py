# Generated by Django 4.0.6 on 2022-08-12 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_inscricao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscricao',
            name='pontos',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
