from django.db import models
from setup.models import SetupCompany
from employees.models import HrEmployee
# Create your models here.
class HrAttendance(models.Model):
    attendance_id = models.BigAutoField(db_column='Attendance_ID', primary_key=True)  # Field name made lowercase.
    emp = models.ForeignKey('employees.HrEmployee', models.DO_NOTHING, db_column='Emp_ID')  # Field name made lowercase.
    company = models.ForeignKey('setup.SetupCompany', models.DO_NOTHING, db_column='Company_ID')  # Field name made lowercase.
    attendance_date = models.DateField(db_column='Attendance_Date')  # Field name made lowercase.
    clock_in = models.TimeField(db_column='Clock_In', blank=True, null=True)  # Field name made lowercase.
    clock_out = models.TimeField(db_column='Clock_Out', blank=True, null=True)  # Field name made lowercase.
    shift_code = models.CharField(db_column='Shift_Code', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    work_hours = models.IntegerField(db_column='Work_Hours', blank=True, null=True)  # Field name made lowercase.
    overtime_hours = models.IntegerField(db_column='Overtime_Hours', blank=True, null=True)  # Field name made lowercase.
    late_minutes = models.IntegerField(db_column='Late_Minutes', blank=True, null=True)  # Field name made lowercase.
    early_minutes = models.IntegerField(db_column='Early_Minutes', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    machine_ip = models.CharField(db_column='Machine_IP', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    modified_by = models.IntegerField(db_column='Modified_By', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HR_Attendance'
        unique_together = (('emp', 'attendance_date', 'shift_code'),)