# Generated by Django 2.2.13 on 2021-01-03 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(null=True, upload_to='')),
                ('brand', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('car_make', models.CharField(max_length=100, null=True)),
                ('price', models.IntegerField(null=True)),
                ('fuel', models.CharField(max_length=20, null=True)),
                ('dimensions', models.CharField(max_length=50, null=True)),
                ('transmission', models.CharField(max_length=100, null=True)),
                ('gears', models.IntegerField(null=True)),
                ('seats', models.IntegerField(null=True)),
                ('power', models.IntegerField(null=True)),
                ('tank_capacity', models.IntegerField(null=True)),
                ('engine_displacement', models.IntegerField(null=True)),
                ('description', models.TextField()),
                ('added_by', models.ForeignKey(null=True, on_delete=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TestDrive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField()),
                ('approved', models.BooleanField(default=False)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('address', models.TextField()),
                ('is_delivered', models.BooleanField(default=False)),
                ('approved_by', models.ForeignKey(null=True, on_delete=None, related_name='approved_by_user', to=settings.AUTH_USER_MODEL)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]