# Generated by Django 5.1.1 on 2024-09-07 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_ticket_venue_ticket_slot'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='venue',
            field=models.CharField(default='', max_length=50),
        ),
    ]
