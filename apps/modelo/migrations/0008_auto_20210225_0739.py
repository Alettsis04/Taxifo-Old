# Generated by Django 3.1.4 on 2021-02-25 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0007_auto_20210225_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='calle1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='calle2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='referencia2',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
