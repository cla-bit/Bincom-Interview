# Generated by Django 4.1 on 2022-12-07 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgentName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='Last Name')),
                ('user_email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('pollingunit_uniqueid', models.SmallIntegerField(blank=True, default=0, verbose_name='Polling Unit Unique ID')),
            ],
        ),
        migrations.CreateModel(
            name='AnnouncedLgaResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='AnnouncedPuResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='AnnouncedStateResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='AnnouncedWardResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Lga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lga_id', models.SmallIntegerField(blank=True, default=0, verbose_name='LGA ID')),
                ('lga_name', models.CharField(blank=True, max_length=30, verbose_name='LGA Name')),
            ],
            options={
                'ordering': ['lga_id'],
            },
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_name', models.CharField(blank=True, max_length=10, verbose_name='Party Name')),
                ('party_score', models.SmallIntegerField(blank=True, default=0, verbose_name='Party Score')),
            ],
            options={
                'ordering': ['party_name'],
            },
        ),
        migrations.CreateModel(
            name='PollingUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll_unique_id', models.SmallIntegerField(blank=True, default=0, verbose_name='Poll Unique Id')),
                ('unique_ward_id', models.SmallIntegerField(blank=True, default=0, verbose_name='Unique Ward IDr')),
                ('polling_unit_number', models.SmallIntegerField(blank=True, default=0, verbose_name='Polling Unit Number')),
                ('polling_unit_name', models.CharField(blank=True, max_length=30, verbose_name='Polling Unit Name')),
                ('polling_unit_desc', models.CharField(blank=True, max_length=30, verbose_name='Polling Unit Description')),
                ('latitude', models.DecimalField(decimal_places=1, default=0, max_digits=12)),
                ('longitude', models.DecimalField(decimal_places=1, default=0, max_digits=12)),
            ],
            options={
                'ordering': ['poll_unique_id'],
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_id', models.SmallIntegerField(blank=True, default=0, verbose_name='State ID')),
                ('state', models.CharField(blank=True, max_length=30, verbose_name='State')),
            ],
            options={
                'ordering': ['-state_id'],
            },
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=10, null=True, verbose_name='Voter')),
                ('user_ip_addr', models.GenericIPAddressField(unpack_ipv4=True, verbose_name="Voter's IP")),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['user_name'],
            },
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward_id', models.SmallIntegerField(blank=True, default=0, verbose_name='Ward ID')),
                ('ward_name', models.CharField(blank=True, max_length=50, verbose_name='Ward Name')),
                ('ward_desc', models.CharField(blank=True, max_length=50, verbose_name='Ward Description')),
                ('lga_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.lga')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.voter')),
            ],
            options={
                'ordering': ['-ward_id'],
            },
        ),
        migrations.AddIndex(
            model_name='voter',
            index=models.Index(fields=['-date_entered'], name='poll_voter_date_en_0000f3_idx'),
        ),
        migrations.AddIndex(
            model_name='voter',
            index=models.Index(fields=['user_ip_addr'], name='poll_voter_user_ip_4df8bc_idx'),
        ),
        migrations.AddIndex(
            model_name='state',
            index=models.Index(fields=['state'], name='poll_state_state_b6545d_idx'),
        ),
        migrations.AddField(
            model_name='pollingunit',
            name='lga_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.lga'),
        ),
        migrations.AddField(
            model_name='pollingunit',
            name='ward_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.ward'),
        ),
        migrations.AddIndex(
            model_name='party',
            index=models.Index(fields=['party_name'], name='poll_party_party_n_1d0fa6_idx'),
        ),
        migrations.AddField(
            model_name='lga',
            name='state_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.state'),
        ),
        migrations.AddField(
            model_name='lga',
            name='voter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.voter'),
        ),
        migrations.AddField(
            model_name='announcedwardresult',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.party'),
        ),
        migrations.AddField(
            model_name='announcedwardresult',
            name='voter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.voter'),
        ),
        migrations.AddField(
            model_name='announcedwardresult',
            name='ward_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.ward'),
        ),
        migrations.AddField(
            model_name='announcedstateresult',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.party'),
        ),
        migrations.AddField(
            model_name='announcedstateresult',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.state'),
        ),
        migrations.AddField(
            model_name='announcedstateresult',
            name='voter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.voter'),
        ),
        migrations.AddField(
            model_name='announcedpuresult',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.party'),
        ),
        migrations.AddField(
            model_name='announcedpuresult',
            name='polling_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.pollingunit'),
        ),
        migrations.AddField(
            model_name='announcedpuresult',
            name='voter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.voter'),
        ),
        migrations.AddField(
            model_name='announcedlgaresult',
            name='lga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.lga'),
        ),
        migrations.AddField(
            model_name='announcedlgaresult',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.party'),
        ),
        migrations.AddField(
            model_name='announcedlgaresult',
            name='voter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.voter'),
        ),
        migrations.AddIndex(
            model_name='ward',
            index=models.Index(fields=['ward_name'], name='poll_ward_ward_na_3f532a_idx'),
        ),
        migrations.AddIndex(
            model_name='pollingunit',
            index=models.Index(fields=['polling_unit_name'], name='poll_pollin_polling_f6df19_idx'),
        ),
        migrations.AddIndex(
            model_name='lga',
            index=models.Index(fields=['lga_id'], name='poll_lga_lga_id_80bbda_idx'),
        ),
        migrations.AddIndex(
            model_name='lga',
            index=models.Index(fields=['lga_name'], name='poll_lga_lga_nam_424f30_idx'),
        ),
    ]
