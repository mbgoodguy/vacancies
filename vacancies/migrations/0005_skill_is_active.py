# Generated by Django 4.2.3 on 2023-07-26 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0004_alter_skill_options_alter_vacancy_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
