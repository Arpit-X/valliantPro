# Generated by Django 2.1.4 on 2018-12-11 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_events_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participations',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.UserProfile'),
        ),
    ]
