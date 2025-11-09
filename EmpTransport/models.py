from django.db import models
from setup.models import SetupCompany
from employees.models import HrEmployee

# Create your models here.
class HrEmpTransport(models.Model):
    transport_id = models.AutoField(db_column='Transport_ID', primary_key=True)  # Field name made lowercase.
    emp = models.ForeignKey('employees.HrEmployee', models.DO_NOTHING, db_column='Emp_ID')  # Field name made lowercase.
    car_plate = models.CharField(db_column='Car_Plate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    car_model = models.CharField(db_column='Car_Model', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pickup_point = models.CharField(db_column='Pickup_Point', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pickup_time = models.TimeField(db_column='Pickup_Time', blank=True, null=True)  # Field name made lowercase.
    drop_time = models.TimeField(db_column='Drop_Time', blank=True, null=True)  # Field name made lowercase.
    driver_name = models.CharField(db_column='Driver_Name', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    is_active = models.BooleanField(db_column='Is_Active')  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    modified_by = models.IntegerField(db_column='Modified_By', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HR_Emp_Transport'