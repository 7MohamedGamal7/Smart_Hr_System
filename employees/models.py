from django.db import models
# from employees.models import HrEmployee
# Create your models here.
class HrEmployee(models.Model):
    emp_id = models.AutoField(db_column='Emp_ID', primary_key=True)  # Field name made lowercase.
    emp_code = models.CharField(db_column='Emp_Code', unique=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    first_name_ar = models.CharField(db_column='First_Name_AR', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    second_name_ar = models.CharField(db_column='Second_Name_AR', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    third_name_ar = models.CharField(db_column='Third_Name_AR', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    last_name_ar = models.CharField(db_column='Last_Name_AR', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    full_name_ar = models.CharField(db_column='Full_Name_AR', max_length=203, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    first_name_en = models.CharField(db_column='First_Name_EN', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    second_name_en = models.CharField(db_column='Second_Name_EN', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    third_name_en = models.CharField(db_column='Third_Name_EN', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    last_name_en = models.CharField(db_column='Last_Name_EN', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    full_name_en = models.CharField(db_column='Full_Name_EN', max_length=203, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    date_birth = models.DateField(db_column='Date_Birth', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nationality = models.CharField(db_column='Nationality', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    national_id = models.CharField(db_column='National_ID', max_length=14, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    personal_id_expiry = models.DateField(db_column='Personal_ID_Expiry', blank=True, null=True)  # Field name made lowercase.
    marital_status = models.CharField(db_column='Marital_Status', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    military_status = models.CharField(db_column='Military_Status', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    phone2 = models.CharField(db_column='Phone2', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email_personal = models.CharField(db_column='Email_Personal', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email_official = models.CharField(db_column='Email_Official', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    address_country = models.CharField(db_column='Address_Country', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    address_governorate = models.CharField(db_column='Address_Governorate', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    address_city = models.CharField(db_column='Address_City', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    address_street = models.CharField(db_column='Address_Street', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    emergency_contact = models.CharField(db_column='Emergency_Contact', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    emergency_phone = models.CharField(db_column='Emergency_Phone', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    has_special_needs = models.BooleanField(db_column='Has_Special_Needs', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    is_active = models.BooleanField(db_column='Is_Active')  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    modified_by = models.IntegerField(db_column='Modified_By', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_Date', blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey('accounts.SecurityUsers', models.DO_NOTHING, db_column='User_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HR_Employee'


class HrEmployeeAssignment(models.Model):
    assignment_id = models.AutoField(db_column='Assignment_ID', primary_key=True)  # Field name made lowercase.
    emp = models.ForeignKey('employees.HrEmployee', models.DO_NOTHING, db_column='Emp_ID')  # Field name made lowercase.
    company = models.ForeignKey('setup.SetupCompany', models.DO_NOTHING, db_column='Company_ID')  # Field name made lowercase.
    dept = models.ForeignKey('Department.SetupDepartment', models.DO_NOTHING, db_column='Dept_ID')  # Field name made lowercase.
    job = models.ForeignKey('Jops.SetupJob', models.DO_NOTHING, db_column='Job_ID')  # Field name made lowercase.
    direct_manager = models.ForeignKey('employees.HrEmployee', models.DO_NOTHING, db_column='Direct_Manager_ID', related_name='hremployeeassignment_direct_manager_set', blank=True, null=True)  # Field name made lowercase.
    employment_type = models.CharField(db_column='Employment_Type', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    hiring_date = models.DateField(db_column='Hiring_Date')  # Field name made lowercase.
    probation_months = models.IntegerField(db_column='Probation_Months', blank=True, null=True)  # Field name made lowercase.
    probation_end_date = models.DateField(db_column='Probation_End_Date', blank=True, null=True)  # Field name made lowercase.
    contract_start = models.DateField(db_column='Contract_Start', blank=True, null=True)  # Field name made lowercase.
    contract_end = models.DateField(db_column='Contract_End', blank=True, null=True)  # Field name made lowercase.
    basic_salary = models.DecimalField(db_column='Basic_Salary', max_digits=18, decimal_places=2)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    shift_type = models.CharField(db_column='Shift_Type', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    current_week_shift = models.CharField(db_column='Current_Week_Shift', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    next_week_shift = models.CharField(db_column='Next_Week_Shift', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    friday_operation = models.CharField(db_column='Friday_Operation', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    is_current = models.BooleanField(db_column='Is_Current')  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    modified_by = models.IntegerField(db_column='Modified_By', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HR_Employee_Assignment'


class HrContract(models.Model):
    contract_id = models.BigAutoField(db_column='Contract_ID', primary_key=True)  # Field name made lowercase.
    emp = models.ForeignKey('employees.HrEmployee', models.DO_NOTHING, db_column='Emp_ID')  # Field name made lowercase.
    contract_no = models.CharField(db_column='Contract_No', unique=True, max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    contract_type = models.CharField(db_column='Contract_Type', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    start_date = models.DateField(db_column='Start_Date')  # Field name made lowercase.
    end_date = models.DateField(db_column='End_Date', blank=True, null=True)  # Field name made lowercase.
    duration_months = models.IntegerField(db_column='Duration_Months', blank=True, null=True)  # Field name made lowercase.
    renewal_count = models.IntegerField(db_column='Renewal_Count')  # Field name made lowercase.
    salary_basic = models.DecimalField(db_column='Salary_Basic', max_digits=18, decimal_places=2)  # Field name made lowercase.
    salary_gross = models.DecimalField(db_column='Salary_Gross', max_digits=18, decimal_places=2)  # Field name made lowercase.
    notice_period_days = models.IntegerField(db_column='Notice_Period_Days', blank=True, null=True)  # Field name made lowercase.
    probation_period = models.IntegerField(db_column='Probation_Period', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    file_attachment = models.BinaryField(db_column='File_Attachment', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    modified_by = models.IntegerField(db_column='Modified_By', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HR_Contract'


class HrEmpDocument(models.Model):
    doc_id = models.BigAutoField(db_column='Doc_ID', primary_key=True)  # Field name made lowercase.
    emp = models.ForeignKey('employees.HrEmployee', models.DO_NOTHING, db_column='Emp_ID')  # Field name made lowercase.
    doc_type = models.ForeignKey('EmpDocument.SetupDocumentType', models.DO_NOTHING, db_column='Doc_Type_ID')  # Field name made lowercase.
    doc_number = models.CharField(db_column='Doc_Number', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    issue_date = models.DateField(db_column='Issue_Date', blank=True, null=True)  # Field name made lowercase.
    expiry_date = models.DateField(db_column='Expiry_Date', blank=True, null=True)  # Field name made lowercase.
    remaining_days = models.IntegerField(db_column='Remaining_Days', blank=True, null=True)  # Field name made lowercase.
    file_attachment = models.BinaryField(db_column='File_Attachment', blank=True, null=True)  # Field name made lowercase.
    is_received = models.BooleanField(db_column='Is_Received')  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    modified_by = models.IntegerField(db_column='Modified_By', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HR_Emp_Document'



class HrEmpFamily(models.Model):
    family_id = models.AutoField(db_column='Family_ID', primary_key=True)  # Field name made lowercase.
    emp = models.ForeignKey('employees.HrEmployee', models.DO_NOTHING, db_column='Emp_ID')  # Field name made lowercase.
    name_ar = models.CharField(db_column='Name_AR', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    name_en = models.CharField(db_column='Name_EN', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    relation = models.CharField(db_column='Relation', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    date_birth = models.DateField(db_column='Date_Birth', blank=True, null=True)  # Field name made lowercase.
    national_id = models.CharField(db_column='National_ID', max_length=14, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    has_insurance = models.BooleanField(db_column='Has_Insurance', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    modified_by = models.IntegerField(db_column='Modified_By', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HR_Emp_Family'