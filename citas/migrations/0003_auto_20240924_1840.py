# Generated by Django 3.1 on 2024-09-24 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0002_auto_20240924_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='codigo_empleado',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
