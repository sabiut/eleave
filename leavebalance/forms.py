from django.contrib.auth.models import User, UserManager
from django.db import models
from django.contrib.auth.models import User
from django import forms

from leavebalance.models import leavecurrentbalance
from leavebalance.models import staffencashment
from leavebalance.models import uploadfile

#calculate current leave balance form

class currentleavebalanceform(forms.ModelForm):
	class Meta:
		model=leavecurrentbalance
		fields=('Leave_current_balance','Total_working_days')


class update_encashment_form(forms.ModelForm):
	class Meta:
		model=leavecurrentbalance
		fields=('Leave_current_balance','leave_encashment')


class staffencashmentform(forms.ModelForm):
	class Meta:
		model=staffencashment
		fields=('First_Name','Last_Name','Payment_date','Payment_date','Number_of_days_paid','cheque_number','Payment_amount','encashment_updated_by')


#uploading file form
class uploadfileform(forms.ModelForm):
	class Meta:
		model=uploadfile
		fields=('description','Select_File')
