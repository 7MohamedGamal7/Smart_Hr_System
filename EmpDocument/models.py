from django.db import models
from setup.models import SetupCompany
from employees.models import HrEmployee
# Create your models here.
class SetupDocumentType(models.Model):
    doc_type_id = models.AutoField(db_column='Doc_Type_ID', primary_key=True)  # Field name made lowercase.
    company = models.ForeignKey('setup.SetupCompany', models.DO_NOTHING, db_column='Company_ID')  # Field name made lowercase.
    doc_code = models.CharField(db_column='Doc_Code', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    doc_name_ar = models.CharField(db_column='Doc_Name_AR', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    doc_name_en = models.CharField(db_column='Doc_Name_EN', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    is_mandatory = models.BooleanField(db_column='Is_Mandatory')  # Field name made lowercase.
    expiry_alert_days = models.IntegerField(db_column='Expiry_Alert_Days', blank=True, null=True)  # Field name made lowercase.
    is_active = models.BooleanField(db_column='Is_Active')  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    modified_by = models.IntegerField(db_column='Modified_By', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Setup_Document_Type'
        unique_together = (('company', 'doc_code'),)