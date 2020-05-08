# Generated by Django 3.0.6 on 2020-05-05 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans19', '0011_auto_20200430_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='case_number',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Case Number'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_id',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Patient Identity Document Number'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
    ]
