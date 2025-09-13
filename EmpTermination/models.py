from django.db import models

from setup.models import SetupCompany
from employees.models import HrEmployee
# Create your models here.
class HrTermination(models.Model):
    termination_id = models.BigAutoField(db_column='Termination_ID', primary_key=True)  # Field name made lowercase.
    emp = models.ForeignKey('employees.HrEmployee', models.DO_NOTHING, db_column='Emp_ID')  # Field name made lowercase.
    request_date = models.DateField(db_column='Request_Date')  # Field name made lowercase.
    last_working_date = models.DateField(db_column='Last_Working_Date')  # Field name made lowercase.
    reason_type = models.CharField(db_column='Reason_Type', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reason_details = models.CharField(db_column='Reason_Details', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    notice_period_days = models.IntegerField(db_column='Notice_Period_Days', blank=True, null=True)  # Field name made lowercase.
    notice_end_date = models.DateField(db_column='Notice_End_Date', blank=True, null=True)  # Field name made lowercase.
    settlement_amount = models.DecimalField(db_column='Settlement_Amount', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    settlement_paid = models.BooleanField(db_column='Settlement_Paid')  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    modified_by = models.IntegerField(db_column='Modified_By', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HR_Termination'