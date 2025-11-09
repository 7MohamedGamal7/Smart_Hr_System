from django.db import models
from employees.models import HrEmployee
from setup.models import SetupCompany

# Create your models here.
class HrSocialInsurance(models.Model):
    si_id = models.BigAutoField(db_column='SI_ID', primary_key=True)  # Field name made lowercase.
    emp = models.ForeignKey('employees.HrEmployee', models.DO_NOTHING, db_column='Emp_ID')  # Field name made lowercase.
    insurance_no = models.CharField(db_column='Insurance_No', unique=True, max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    form_s1_received = models.BooleanField(db_column='Form_S1_Received')  # Field name made lowercase.
    form_s1_date = models.DateField(db_column='Form_S1_Date', blank=True, null=True)  # Field name made lowercase.
    form_s6_received = models.BooleanField(db_column='Form_S6_Received')  # Field name made lowercase.
    form_s6_date = models.DateField(db_column='Form_S6_Date', blank=True, null=True)  # Field name made lowercase.
    subscription_date = models.DateField(db_column='Subscription_Date', blank=True, null=True)  # Field name made lowercase.
    subscription_salary = models.DecimalField(db_column='Subscription_Salary', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    employee_percent = models.DecimalField(db_column='Employee_Percent', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    company_percent = models.DecimalField(db_column='Company_Percent', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    exit_date = models.DateField(db_column='Exit_Date', blank=True, null=True)  # Field name made lowercase.
    exit_reason = models.CharField(db_column='Exit_Reason', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    modified_by = models.IntegerField(db_column='Modified_By', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HR_Social_Insurance'