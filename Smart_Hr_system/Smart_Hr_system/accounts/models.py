from django.db import models

# Create your models here.
class SecurityUsers(models.Model):
    user_id = models.AutoField(db_column='User_ID', primary_key=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='User_Name', unique=True, max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    full_name = models.CharField(db_column='Full_Name', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    password_hash = models.CharField(db_column='Password_Hash', max_length=64, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    is_active = models.BooleanField(db_column='Is_Active')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Security_Users'