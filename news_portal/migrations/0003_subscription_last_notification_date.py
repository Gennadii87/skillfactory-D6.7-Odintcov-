# Generated by Django 4.2 on 2023-05-29 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_portal', '0002_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='last_notification_date',
            field=models.DateTimeField(null=True),
        ),
    ]