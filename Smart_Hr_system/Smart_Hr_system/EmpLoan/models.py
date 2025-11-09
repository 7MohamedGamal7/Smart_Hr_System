from django.db import models
from setup.models import SetupCompany
from employees.models import HrEmployee

# Create your models here.
class SetupLoanDeductionType(models.Model):
    type_id = models.AutoField(db_column='Type_ID', primary_key=True)  # Field name made lowercase.
    company = models.ForeignKey('setup.SetupCompany', models.DO_NOTHING, db_column='Company_ID')  # Field name made lowercase.
    type_code = models.CharField(db_column='Type_Code', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    type_name_ar = models.CharField(db_column='Type_Name_AR', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    type_name_en = models.CharField(db_column='Type_Name_EN', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    is_loan = models.BooleanField(db_column='Is_Loan')  # Field name made lowercase.
    max_amount = models.DecimalField(db_column='Max_Amount', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    max_installment = models.IntegerField(db_column='Max_Installment', blank=True, null=True)  # Field name made lowercase.
    interest_rate = models.DecimalField(db_column='Interest_Rate', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    is_active = models.BooleanField(db_column='Is_Active')  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    modified_by = models.IntegerField(db_column='Modified_By', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Setup_Loan_Deduction_Type'
        unique_together = (('company', 'type_code'),)




class HrEmpLoan(models.Model):
    loan_id = models.AutoField(db_column='Loan_ID', primary_key=True)  # Field name made lowercase.
    emp = models.ForeignKey('employees.HrEmployee', models.DO_NOTHING, db_column='Emp_ID')  # Field name made lowercase.
    type = models.ForeignKey('EmpLoan.SetupLoanDeductionType', models.DO_NOTHING, db_column='Type_ID')  # Field name made lowercase.
    request_date = models.DateField(db_column='Request_Date')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=2)  # Field name made lowercase.
    installment_count = models.IntegerField(db_column='Installment_Count')  # Field name made lowercase.
    interest_rate = models.DecimalField(db_column='Interest_Rate', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    monthly_amount = models.DecimalField(db_column='Monthly_Amount', max_digits=29, decimal_places=13, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    approved_by = models.ForeignKey('employees.HrEmployee', models.DO_NOTHING, db_column='Approved_By', related_name='hremploan_approved_by_set', blank=True, null=True)  # Field name made lowercase.
    approved_date = models.DateTimeField(db_column='Approved_Date', blank=True, null=True)  # Field name made lowercase.
    first_deduct_date = models.DateField(db_column='First_Deduct_Date', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    modified_by = models.IntegerField(db_column='Modified_By', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HR_Emp_Loan'



