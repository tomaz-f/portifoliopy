# Generated by Django 3.1.7 on 2022-08-13 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_rename_projects_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]