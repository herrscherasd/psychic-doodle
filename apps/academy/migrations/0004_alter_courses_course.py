# Generated by Django 4.2.1 on 2023-05-10 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0003_alter_courses_options_alter_courses_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course',
            field=models.CharField(max_length=100, verbose_name='Выбор направления'),
        ),
    ]
