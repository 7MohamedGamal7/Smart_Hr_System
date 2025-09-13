from django.db import models
from setup.models import SetupCompany
# Create your models here.
class SetupDepartment(models.Model):
    dept_id = models.AutoField(db_column='Dept_ID', primary_key=True)  # Field name made lowercase.
    company = models.ForeignKey('setup.SetupCompany', models.DO_NOTHING, db_column='Company_ID')  # Field name made lowercase.
    parent_dept = models.ForeignKey('self', models.DO_NOTHING, db_column='Parent_Dept_ID', blank=True, null=True)  # Field name made lowercase.
    dept_code = models.CharField(db_column='Dept_Code', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    dept_name_ar = models.CharField(db_column='Dept_Name_AR', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    dept_name_en = models.CharField(db_column='Dept_Name_EN', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    manager_emp_id = models.IntegerField(db_column='Manager_Emp_ID', blank=True, null=True)  # Field name made lowercase.
    is_active = models.BooleanField(db_column='Is_Active')  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    modified_by = models.IntegerField(db_column='Modified_By', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Setup_Department'
        unique_together = (('company', 'dept_code'),)