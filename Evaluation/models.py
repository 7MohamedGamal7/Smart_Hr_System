from django.db import models
from employees.models import HrEmployee  # ✅ صحيح

from setup.models import SetupCompany
# Create your models here.

class SetupEvaluationType(models.Model):
    eval_type_id = models.AutoField(db_column='Eval_Type_ID', primary_key=True)  # Field name made lowercase.
    company = models.ForeignKey('setup.SetupCompany', models.DO_NOTHING, db_column='Company_ID')  # Field name made lowercase.
    eval_code = models.CharField(db_column='Eval_Code', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    eval_name_ar = models.CharField(db_column='Eval_Name_AR', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    eval_name_en = models.CharField(db_column='Eval_Name_EN', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    frequency_months = models.IntegerField(db_column='Frequency_Months')  # Field name made lowercase.
    is_active = models.BooleanField(db_column='Is_Active')  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    modified_by = models.IntegerField(db_column='Modified_By', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Setup_Evaluation_Type'
        unique_together = (('company', 'eval_code'),)





class HrEmpEvaluation(models.Model):
    evaluation_id = models.AutoField(db_column='Evaluation_ID', primary_key=True)  # Field name made lowercase.
    emp = models.ForeignKey('employees.HrEmployee', models.DO_NOTHING, db_column='Emp_ID')  # Field name made lowercase.
    eval_type = models.ForeignKey('Evaluation.SetupEvaluationType', models.DO_NOTHING, db_column='Eval_Type_ID')  # Field name made lowercase.
    eval_date = models.DateField(db_column='Eval_Date')  # Field name made lowercase.
    eval_period_from = models.DateField(db_column='Eval_Period_From')  # Field name made lowercase.
    eval_period_to = models.DateField(db_column='Eval_Period_To')  # Field name made lowercase.
    total_score = models.DecimalField(db_column='Total_Score', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    grade = models.CharField(db_column='Grade', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    recommendations = models.CharField(db_column='Recommendations', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    approved_by = models.ForeignKey('employees.HrEmployee', models.DO_NOTHING, db_column='Approved_By', related_name='hrempevaluation_approved_by_set', blank=True, null=True)  # Field name made lowercase.
    approved_date = models.DateTimeField(db_column='Approved_Date', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    modified_by = models.IntegerField(db_column='Modified_By', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HR_Emp_Evaluation'