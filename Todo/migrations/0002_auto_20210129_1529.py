# Generated by Django 3.1.5 on 2021-01-29 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Conse',
        ),
        migrations.AlterModelOptions(
            name='conse',
            options={'managed': True, 'verbose_name': 'conse', 'verbose_name_plural': 'conses'},
        ),
        migrations.AlterModelTable(
            name='conse',
            table='Conse',
        ),
    ]
