# Generated by Django 2.0.3 on 2018-10-12 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0002_livro_obs'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='data_cadastro',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
