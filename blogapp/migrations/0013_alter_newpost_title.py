# Generated by Django 4.2.7 on 2023-11-04 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0012_alter_profilepage_bio_alter_profilepage_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpost',
            name='title',
            field=models.CharField(blank=True, null=True),
        ),
    ]
