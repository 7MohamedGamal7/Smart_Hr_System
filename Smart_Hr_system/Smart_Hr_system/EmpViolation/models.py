from django.db import models
from employees.models import HrEmployee  # ✅ صحيح
from setup.models import SetupCompany
# Create your models here.


class SetupViolationType(models.Model):
    violation_id = models.AutoField(db_column='Violation_ID', primary_key=True)  # Field name made lowercase.
    company = models.ForeignKey('setup.SetupCompany', models.DO_NOTHING, db_column='Company_ID')  # Field name made lowercase.
    violation_code = models.CharField(db_column='Violation_Code', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    violation_name = models.CharField(db_column='Violation_Name', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    penalty_type = models.CharField(db_column='Penalty_Type', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    penalty_days = models.IntegerField(db_column='Penalty_Days', blank=True, null=True)  # Field name made lowercase.
    penalty_amount = models.DecimalField(db_column='Penalty_Amount', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    is_active = models.BooleanField(db_column='Is_Active')  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    modified_by = models.IntegerField(db_column='Modified_By', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Setup_Violation_Type'
        unique_together = (('company', 'violation_code'),)






class HrEmpViolation(models.Model):
    emp_violation_id = models.BigAutoField(db_column='Emp_Violation_ID', primary_key=True)  # Field name made lowercase.
    emp = models.ForeignKey('employees.HrEmployee', models.DO_NOTHING, db_column='Emp_ID')  # Field name made lowercase.
    violation = models.ForeignKey('EmpViolation.SetupViolationType', models.DO_NOTHING, db_column='Violation_ID')  # Field name made lowercase.
    violation_date = models.DateField(db_column='Violation_Date')  # Field name made lowercase.
    details = models.CharField(db_column='Details', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    penalty_executed = models.BooleanField(db_column='Penalty_Executed')  # Field name made lowercase.
    executed_date = models.DateTimeField(db_column='Executed_Date', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    modified_by = models.IntegerField(db_column='Modified_By', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HR_Emp_Violation'



