# Generated by Django 3.1.13 on 2022-10-07 07:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HospitalApp', '0003_auto_20221004_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_doctor_register',
            fields=[
                ('DoctorID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=512)),
                ('email', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=15)),
                ('education', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
