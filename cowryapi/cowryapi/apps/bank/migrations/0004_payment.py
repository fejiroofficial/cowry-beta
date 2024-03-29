# Generated by Django 2.0 on 2019-12-10 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_auto_20191208_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_round', models.IntegerField()),
                ('amount_paid', models.FloatField()),
                ('amount_debt', models.FloatField()),
                ('payment_date', models.DateTimeField(auto_now=True)),
                ('bank_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.BankMembers')),
            ],
        ),
    ]
