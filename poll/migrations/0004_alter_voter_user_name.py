# Generated by Django 4.1 on 2022-12-07 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_alter_voter_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='user_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Voter'),
        ),
    ]
