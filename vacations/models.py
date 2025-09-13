from django.db import models
from setup.models import SetupCompany
from employees.models import HrEmployee  # ✅ صحيح

# Create your models here.

class SetupLeaveType(models.Model):
    leave_type_id = models.AutoField(db_column='Leave_Type_ID', primary_key=True)  # Field name made lowercase.
    company = models.ForeignKey('setup.SetupCompany',on_delete=models.DO_NOTHING, db_column='Company_ID')  # Field name made lowercase.
    leave_code = models.CharField(db_column='Leave_Code', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    leave_name_ar = models.CharField(db_column='Leave_Name_AR', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    leave_name_en = models.CharField(db_column='Leave_Name_EN', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    paid_unpaid = models.CharField(db_column='Paid_Unpaid', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    max_days_year = models.IntegerField(db_column='Max_Days_Year')  # Field name made lowercase.
    carry_forward = models.BooleanField(db_column='Carry_Forward')  # Field name made lowercase.
    max_carry = models.IntegerField(db_column='Max_Carry', blank=True, null=True)  # Field name made lowercase.
    gender_limit = models.CharField(db_column='Gender_Limit', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    is_active = models.BooleanField(db_column='Is_Active')  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    modified_by = models.IntegerField(db_column='Modified_By', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Setup_Leave_Type'
        unique_together = (('company', 'leave_code'),)


class SetupHoliday(models.Model):
    holiday_id = models.AutoField(db_column='Holiday_ID', primary_key=True)  # Field name made lowercase.
    company = models.ForeignKey('setup.SetupCompany', models.DO_NOTHING, db_column='Company_ID')  # Field name made lowercase.
    holiday_date = models.DateField(db_column='Holiday_Date')  # Field name made lowercase.
    holiday_name_ar = models.CharField(db_column='Holiday_Name_AR', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    holiday_name_en = models.CharField(db_column='Holiday_Name_EN', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    is_recurring = models.BooleanField(db_column='Is_Recurring')  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Setup_Holiday'
        unique_together = (('company', 'holiday_date'),)




class HrEmpLeaveBalance(models.Model):
    balance_id = models.AutoField(db_column='Balance_ID', primary_key=True)  # Field name made lowercase.
    emp = models.ForeignKey('employees.HrEmployee', models.DO_NOTHING, db_column='Emp_ID')  # Field name made lowercase.
    leave_type = models.ForeignKey('vacations.SetupLeaveType', models.DO_NOTHING, db_column='Leave_Type_ID')  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    opening_balance = models.IntegerField(db_column='Opening_Balance')  # Field name made lowercase.
    consumed_days = models.IntegerField(db_column='Consumed_Days')  # Field name made lowercase.
    remaining_balance = models.IntegerField(db_column='Remaining_Balance', blank=True, null=True)  # Field name made lowercase.
    carry_forward_days = models.IntegerField(db_column='Carry_Forward_Days')  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    modified_by = models.IntegerField(db_column='Modified_By', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HR_Emp_Leave_Balance'
        unique_together = (('emp', 'leave_type', 'year'),)



class HrEmpLeaveRequest(models.Model):
    leave_request_id = models.AutoField(db_column='Leave_Request_ID', primary_key=True)  # Field name made lowercase.
    emp = models.ForeignKey('employees.HrEmployee', models.DO_NOTHING, db_column='Emp_ID')  # Field name made lowercase.
    leave_type = models.ForeignKey('vacations.SetupLeaveType', models.DO_NOTHING, db_column='Leave_Type_ID')  # Field name made lowercase.
    start_date = models.DateField(db_column='Start_Date')  # Field name made lowercase.
    end_date = models.DateField(db_column='End_Date')  # Field name made lowercase.
    days_count = models.IntegerField(db_column='Days_Count')  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    contact_phone = models.CharField(db_column='Contact_Phone', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    contact_address = models.CharField(db_column='Contact_Address', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    approved_by = models.ForeignKey('employees.HrEmployee', models.DO_NOTHING, db_column='Approved_By', related_name='hrempleaverequest_approved_by_set', blank=True, null=True)  # Field name made lowercase.
    approved_date = models.DateTimeField(db_column='Approved_Date', blank=True, null=True)  # Field name made lowercase.
    rejection_reason = models.CharField(db_column='Rejection_Reason', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    modified_by = models.IntegerField(db_column='Modified_By', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HR_Emp_Leave_Request'