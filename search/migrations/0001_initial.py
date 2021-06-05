# Generated by Django 3.2.4 on 2021-06-05 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.CharField(blank=True, db_column='Date', max_length=255, null=True)),
                ('time', models.CharField(blank=True, db_column='Time', max_length=255, null=True)),
                ('usec', models.CharField(blank=True, max_length=255, null=True)),
                ('sourceip', models.CharField(blank=True, db_column='SourceIP', max_length=255, null=True)),
                ('sourceport', models.CharField(blank=True, db_column='SourcePort', max_length=255, null=True)),
                ('destinationip', models.CharField(blank=True, db_column='DestinationIP', max_length=255, null=True)),
                ('destinationport', models.CharField(blank=True, db_column='DestinationPort', max_length=255, null=True)),
                ('dns_a_record_query', models.CharField(blank=True, db_column='DNS_A_record_query', max_length=255, null=True)),
            ],
            options={
                'db_table': 'log',
                'managed': True,
            },
        ),
    ]