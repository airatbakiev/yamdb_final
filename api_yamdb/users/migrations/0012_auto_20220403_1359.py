# Generated by Django 2.2.16 on 2022-04-03 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20220403_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Код подтверждения'),
        ),
    ]
