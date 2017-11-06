from django.contrib.auth.models import User, UserManager
from django.db import models
from django.contrib.auth.models import User
from django import forms
#from models import staff
#from models import leave
from django.contrib.admin import widgets
import datetime
from models import new_staff
from models import newleave
from models import training
from models import employment_history

#datepicker fix
#from datetimewidget.widgets import DateTimeWidget
import datetime

class leaveapplication2(forms.ModelForm):
    class Meta:
        model =newleave
        fields =('leave_type', 'specify_details', 'start_date', 'end_date', 'total_working_days', 'department_head_authorization', 'authorized_by', 'remarks', 'authorization_date', 'username')


class addstaff(forms.ModelForm):
    class Meta:
        model =new_staff
        fields =('first_name', 'last_name', 'gender', 'date_of_birth', 'marital_status', 'nationality', 'home_island', 'dependants', 'relationship_to_you', 'postal_Address', 'employee_Date', 'position', 'department', 'vnpf_no', 'bank_name', 'account_number')

class train(forms.ModelForm):
    class Meta:
        model = training
        fields =( 'staff_name','institution_num1','qualification_num1','year_of_completion_num1', 'institution_num2','qualification_num2','year_of_completion_num2', 'institution_num3', 'qualification_num3','year_of_completion_num3','highest_qualification',
  'RBV_training1','month','year','RBV_training2','month1','year1','RBV_training3','month2','year2','RBV_training4','month3','year3','RBV_training5','month4','year4','RBV_training6','month5','year5',
                 'RBV_training7','month6','year6','RBV_training8','month6','year6','RBV_training9','month8','year8','RBV_training10','month9','year9','RBV_training11','month10','year10','RBV_training12','month11','year11','RBV_training13','month12','year12',
                'RBV_training14','month13','year13','RBV_training15','month14','year14')


class institution(forms.ModelForm):
    class Meta:
        model = employment_history
        fields =('staff_name','institution_num1','position_num1','start_Date_num1','end_Date_num1','responsibilities_num1', 'institution_num2','position_num2','start_Date_num2','end_Date_num2','responsibilities_num2', 'institution_num3', 'position_num3', 'start_Date_num3', 'end_Date_num3', 'responsibilities_num3')

class leave_application(forms.ModelForm):
   # start_date=forms.DateField(widget=widgets.AdminDateWidget)
    class Meta:
        model =newleave
        fields =('id','first_name', 'last_name', 'department', 'position', 'leave_type', 'specify_details', 'start_date', 'end_date', 'total_working_days','username')


       #form for authorized leave
class authoriseleave(forms.ModelForm):
    class Meta:
        model =newleave
        widgets = {'date': forms.DateInput(attrs={'class': 'datepicker'})}
        fields =('department_head_authorization', 'authorized_by', 'remarks', 'authorization_date')

class coporateservices_authoriseleave(forms.ModelForm):
    class Meta:
        model =newleave
        widgets = {'date': forms.DateInput(attrs={'class': 'datepicker'})}
        fields =('Director_authorization', 'Authorization_by', 'Director_remarks', 'Authoriztaion_date')

#leave calculator
class leavecalculator(forms.ModelForm):
    class Meta:
        model =newleave
        fields =('month', 'year', 'leave_entitlement', 'holiday', 'weekend', 'leave_outstanding_balance')


#leave process form
class processbalanceform(forms.ModelForm):
    class Meta:
        model =newleave
        fields =('process_bal',)
