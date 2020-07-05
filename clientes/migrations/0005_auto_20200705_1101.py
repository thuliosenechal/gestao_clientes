# Generated by Django 3.0.7 on 2020-07-05 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_auto_20200705_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='document',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='clientes.Document'),
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_number', models.CharField(max_length=10)),
                ('sales_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('sales_discount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clientes.Person')),
            ],
        ),
    ]