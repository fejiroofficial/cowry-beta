# Generated by Django 2.0 on 2019-12-05 20:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guarantor_name', models.CharField(max_length=50)),
                ('guarantor_address', models.CharField(max_length=150)),
                ('guarantor_phone', models.CharField(max_length=20)),
                ('guarantor_photo', models.URLField(default='www.profileimage.com')),
                ('is_active', models.BooleanField(default=False)),
                ('joined_on', models.DateField(auto_now=True)),
                ('bank_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_group', to='bank.Bank')),
                ('bank_member', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='bank_member', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
