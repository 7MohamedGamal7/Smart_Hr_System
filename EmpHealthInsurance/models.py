from django.db import models
from employees.models import HrEmployee
from setup.models import SetupCompany


# Create your models here.
class HrHealthInsurance(models.Model):
    hi_id = models.BigAutoField(db_column='HI_ID', primary_key=True)  # Field name made lowercase.
    emp = models.ForeignKey('employees.HrEmployee', models.DO_NOTHING, db_column='emp_id')  # Field name made lowercase.
    provider = models.CharField(db_column='Provider', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    policy_no = models.CharField(db_column='Policy_No', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    card_no = models.CharField(db_column='Card_No', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    start_date = models.DateField(db_column='Start_Date', blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateField(db_column='End_Date', blank=True, null=True)  # Field name made lowercase.
    insurance_job_code = models.CharField(db_column='Insurance_Job_Code', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    insurance_job_name = models.CharField(db_column='Insurance_Job_Name', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    premium_amount = models.DecimalField(db_column='Premium_Amount', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    modified_by = models.IntegerField(db_column='Modified_By', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HR_Health_Insurance'