# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Log(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.CharField(db_column='Date', max_length=255, blank=True, null=True)  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=255, blank=True, null=True)  # Field name made lowercase.
    usec = models.CharField(max_length=255, blank=True, null=True)
    sourceip = models.CharField(db_column='SourceIP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourceport = models.CharField(db_column='SourcePort', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destinationip = models.CharField(db_column='DestinationIP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destinationport = models.CharField(db_column='DestinationPort', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dns_a_record_query = models.CharField(db_column='DNS_A_record_query', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'log'
