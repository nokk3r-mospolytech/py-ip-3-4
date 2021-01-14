# Generated by Django 3.1.5 on 2021-01-14 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210115_0640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avilable',
            name='Priority_id',
        ),
        migrations.RemoveField(
            model_name='avilable',
            name='region_id',
        ),
        migrations.AddField(
            model_name='avilable',
            name='Region_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.region', verbose_name='Регион'),
        ),
    ]
