from django.db import models
from setup.models import SetupCompany
# Create your models here.
class SetupJob(models.Model):
    job_id = models.AutoField(db_column='Job_ID', primary_key=True)  # Field name made lowercase.
    company = models.ForeignKey('setup.SetupCompany', models.DO_NOTHING, db_column='Company_ID')  # Field name made lowercase.
    job_code = models.CharField(db_column='Job_Code', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    job_name_ar = models.CharField(db_column='Job_Name_AR', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    job_name_en = models.CharField(db_column='Job_Name_EN', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    job_description = models.CharField(db_column='Job_Description', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    min_salary = models.DecimalField(db_column='Min_Salary', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    max_salary = models.DecimalField(db_column='Max_Salary', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    is_active = models.BooleanField(db_column='Is_Active')  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    modified_by = models.IntegerField(db_column='Modified_By', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Setup_Job'
        unique_together = (('company', 'job_code'),)