# Generated by Django 2.1.4 on 2018-12-10 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('totalPraticipants', models.IntegerField()),
                ('isSpot', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('longitiude', models.DecimalField(decimal_places=3, max_digits=8)),
                ('latitude', models.DecimalField(decimal_places=3, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Participations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registeredOn', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Events')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('college', models.CharField(default='', max_length=30)),
                ('joinedOn', models.DateTimeField(auto_now_add=True)),
                ('isCoordinator', models.BooleanField(default=False)),
                ('isFaculty', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='events',
            name='facultyCoordinator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facultyCord', to='events.UserProfile'),
        ),
        migrations.AddField(
            model_name='events',
            name='location',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='events.Location'),
        ),
        migrations.AddField(
            model_name='events',
            name='studentCoordinator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentCord', to='events.UserProfile'),
        ),
    ]
