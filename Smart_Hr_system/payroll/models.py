from django.db import models
from employees.models import HrEmployee
from setup.models import SetupCompany

# Create your models here.

class PayrollHeader(models.Model):
    payroll_id = models.BigAutoField(db_column='Payroll_ID', primary_key=True)  # Field name made lowercase.
    company = models.ForeignKey('setup.SetupCompany', models.DO_NOTHING, db_column='Company_ID')  # Field name made lowercase.
    payroll_month = models.DateField(db_column='Payroll_Month')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    processed_date = models.DateTimeField(db_column='Processed_Date', blank=True, null=True)  # Field name made lowercase.
    processed_by = models.IntegerField(db_column='Processed_By', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    modified_by = models.IntegerField(db_column='Modified_By', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payroll_Header'
        unique_together = (('company', 'payroll_month'),)





class PayrollLine(models.Model):
    line_id = models.BigAutoField(db_column='Line_ID', primary_key=True)  # Field name made lowercase.
    payroll = models.ForeignKey('payroll.PayrollHeader', models.DO_NOTHING, db_column='Payroll_ID')  # Field name made lowercase.
    emp = models.ForeignKey('employees.HrEmployee', models.DO_NOTHING, db_column='Emp_ID')  # Field name made lowercase.
    item = models.ForeignKey('payroll.SetupPayrollItem', models.DO_NOTHING, db_column='Item_ID')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=2)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    modified_by = models.IntegerField(db_column='Modified_By', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payroll_Line'



class SetupPayrollItem(models.Model):
    item_id = models.AutoField(db_column='Item_ID', primary_key=True)  # Field name made lowercase.
    company = models.ForeignKey('setup.SetupCompany', models.DO_NOTHING, db_column='Company_ID')  # Field name made lowercase.
    item_code = models.CharField(db_column='Item_Code', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    item_name_ar = models.CharField(db_column='Item_Name_AR', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    item_name_en = models.CharField(db_column='Item_Name_EN', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    item_type = models.CharField(db_column='Item_Type', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    calculation_type = models.CharField(db_column='Calculation_Type', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    default_value = models.DecimalField(db_column='Default_Value', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxable = models.BooleanField(db_column='Taxable')  # Field name made lowercase.
    insurable = models.BooleanField(db_column='Insurable')  # Field name made lowercase.
    is_active = models.BooleanField(db_column='Is_Active')  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    modified_by = models.IntegerField(db_column='Modified_By', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Setup_Payroll_Item'
        unique_together = (('company', 'item_code'),)