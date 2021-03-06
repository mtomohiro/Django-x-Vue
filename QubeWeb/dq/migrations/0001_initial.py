# Generated by Django 3.0.7 on 2020-06-20 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='患者名')),
                ('birth', models.DateField(verbose_name='生年月日')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookDateTime', models.DateTimeField(verbose_name='予約日時')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Books', to='dq.Patient', verbose_name='患者')),
            ],
        ),
    ]
