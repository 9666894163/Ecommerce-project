# Generated by Django 3.2.9 on 2022-01-31 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ecomapp', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('user', models.CharField(max_length=25)),
                ('status', models.BooleanField(default=False)),
                ('item_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecomapp.products')),
            ],
        ),
    ]