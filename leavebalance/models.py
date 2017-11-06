from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User, UserManager
from django.db.models.fields import DateField, DateTimeField
from django.utils import timezone



# Create your models here.

class leavecurrentbalance(models.Model):
	First_Name=models.CharField(max_length=45)
	Last_Name=models.CharField(max_length=45)
	Leave_outstanding_balance=models.CharField(max_length=45)
	Monthly_Leave_entitlement=models.CharField(max_length=45)
	Monthly_leave_consumed=models.CharField(max_length=45)
	Total_working_days=models.CharField(max_length=45,default='')
	Year=models.CharField(max_length=45)
	Month=models.CharField(max_length=45)
	Leave_current_balance=models.CharField(max_length=45)
	department=models.CharField(max_length=45,default="")
	leave_encashment=models.CharField(max_length=45,default='')

	def __unicode__(self):
		return self.First_Name

class staffencashment(models.Model):
	First_Name=models.CharField(max_length=45)
	Last_Name=models.CharField(max_length=45)
	Payment_date=models.CharField(max_length=45)
	Number_of_days_paid=models.IntegerField()
	cheque_number=models.CharField(max_length=45)
	Payment_amount=models.FloatField()
	names=(
	('Kensen','Kensen'),
	('Kenny','Kenny'),
	('Julia','Julia'),


	)
	encashment_updated_by=models.CharField(max_length=45,choices=names,default="")

	def __unicode__(self):
		return self.First_Name

#model to upload file
class uploadfile(models.Model):
	description = models.CharField(max_length=255, blank=True)
	Select_File=models.FileField(upload_to='/var/www/projects/webapp/media')
	uploaded_at =models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.description
