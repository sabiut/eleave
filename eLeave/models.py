from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User, UserManager
from django.db.models.fields import DateField, DateTimeField
from django.utils import timezone

# Create your models here.



#New database
class new_staff(models.Model):
    #staff_id =models.CharField(max_length=45, null=False, default="")
    first_name = models.CharField(max_length=45)
    last_name =models.CharField(max_length=45)

    sex=(
        ('Male', 'Male'),
        ('Female', 'Female'),

    )
    gender =models.CharField(max_length=45, choices=sex, default="")
    date_of_birth =models.DateField(null=True)

    marital=(
        ('Married', 'Married'),
        ('Single', 'Single'),
        ('De Facto','De Facto'),

    )
    marital_status=models.CharField(max_length=45, choices=marital, default="")
    nationality =models.CharField(max_length=45, default="")

    island=(
        ('Banks', 'Banks'),
        ('Santo', 'Santo'),
        ('Ambae', 'Ambae'),
        ('Pentecost', 'Pentecost'),
        ('Maewo', 'Maewo'),
        ('Malekula', 'Malekula'),
        ('Ambrym', 'Ambrym'),
        ('Paama', 'Paama'),
        ('Epi', 'Epi'),
        ('Tongoa', 'Tongoa'),
        ('Tongariki', 'Tongariki'),
        ('Makira', 'Makira'),
        ('Emae', 'Emae'),
        ('Mataso', 'Mataso'),
        ('Efate', 'Efate'),
        ('Erromango', 'Erromango'),
        ('Tanna', 'Tanna'),
        ('Futuna', 'Futuna'),
        ('Aniwa', 'Aniwa'),
        )
    home_island =models.CharField(max_length=45, choices=island, default="")
    dependants=models.TextField(default="")

    #depen=(
       # ('Brother', 'Brother'),
       # ('Sister', 'Sister'),
       # ('Mother', 'Mother'),
       # ('Father', 'Father'),
       # ('Ant', 'Ant'),
       # ('Uncle', 'Uncle'),
       # ('Son', 'Son'),
       # ('Daughter', 'Daughter'),
       # ('nephew', 'nephew'),
    #relationship_to_you =models.CharField(max_length=45, choices=depen, default="")
    relationship_to_you =models.TextField(default="")
    postal_Address=models.TextField(default="")
    employee_Date=models.DateField()
    position=models.CharField(max_length =45)

    depment=(
        ('GOV', 'GOV'),
        ('ACSD', 'ACSD'),
        ('CSD', 'CSD'),
        ('FISD', 'FISD'),
        ('RSD', 'RSD'),
        ('FMKD', 'FMKD'),
    )
    department=models.CharField(max_length =45,  choices= depment, default="")
    vnpf_no =models.CharField(max_length =45)
    bank_name =models.CharField(max_length=45, default="")
    account_number=models.IntegerField()
    username  =models.ForeignKey(User, default =1)

    def __unicode__(self):
        return self.first_name

class training(models.Model):
    institution_num1=models.CharField(max_length=45)
    institution_num2=models.CharField(max_length=45)
    institution_num3=models.CharField(max_length=45)

    qualification1=(
        ('PHD Degree', 'PHD Degree'),
        ('Masters Degree', 'Masters Degree'),
        ('Bachelor Degree', 'Bachelor Degree'),
        ('Diploma', 'Diploma'),
        ('Certificate', 'Certificate'),
        ('Postgraduate Diploma','Postgraduate Diploma'),
        ('none','none')
        )
    qualification_num1=models.CharField(max_length=45, choices=qualification1)
    qualification2=(
        ('PHD Degree', 'PHD Degree'),
        ('Master Degree', 'Master Degree'),
        ('Bachelor Degree', 'Bachelor Degree'),
        ('Diploma', 'Diploma '),
        ('Certificate', 'Certificate'),
        ('Postgraduate Diploma','Postgraduate Diploma'),
        ('none','none')
        )
    qualification_num2=models.CharField(max_length=45, choices=qualification2)
    qualification3=(
        ('PHD Degree', 'PHD Degree'),
        ('Master Degree', 'Master Degree'),
        ('Bachelor Degree', 'Bachelor Degree'),
        ('Diploma', 'Diploma'),
        ('Certificate', 'Certificate '),
        ('Postgraduate Diploma','Postgraduate Diploma'),
        ('none','none')
        )
    qualification_num3=models.CharField(max_length=45,  choices=qualification3)
    highest_qualification=models.CharField(max_length=45)
    year_of_completion_num1=models.CharField(max_length=45)
    year_of_completion_num2=models.CharField(max_length=45)
    year_of_completion_num3=models.CharField(max_length=45)
    RBV_training1=models.CharField(max_length=45,default='')
    month=models.CharField(max_length=45,default='')
    year=models.CharField(max_length=45,default='')
    RBV_training2=models.CharField(max_length=45,default='')
    month1=models.CharField(max_length=45,default='')
    year1=models.CharField(max_length=45,default='')
    RBV_training3=models.CharField(max_length=45,default='')
    month2=models.CharField(max_length=45,default='')
    year2=models.CharField(max_length=45,default='')
    RBV_training4=models.CharField(max_length=45,default='')
    month3=models.CharField(max_length=45,default='')
    year3=models.CharField(max_length=45,default='')
    RBV_training5=models.CharField(max_length=45,default='')
    month4=models.CharField(max_length=45,default='')
    year4=models.CharField(max_length=45,default='')
    RBV_training6=models.CharField(max_length=45,default='')
    month5=models.CharField(max_length=45,default='')
    year5=models.CharField(max_length=45,default='')
    RBV_training7=models.CharField(max_length=45,default='')
    month6=models.CharField(max_length=45,default='')
    year6=models.CharField(max_length=45,default='')
    RBV_training8=models.CharField(max_length=45,default='')
    month7=models.CharField(max_length=45,default='')
    year7=models.CharField(max_length=45,default='')
    RBV_training9=models.CharField(max_length=45,default='')
    month8=models.CharField(max_length=45,default='')
    year8=models.CharField(max_length=45,default='')
    RBV_training10=models.CharField(max_length=45,default='')
    month9=models.CharField(max_length=45,default='')
    year9=models.CharField(max_length=45,default='')
    RBV_training11=models.CharField(max_length=45,default='')
    month10=models.CharField(max_length=45,default='')
    year10=models.CharField(max_length=45,default='')
    RBV_training12=models.CharField(max_length=45,default='')
    month11=models.CharField(max_length=45,default='')
    year11=models.CharField(max_length=45,default='')
    RBV_training13=models.CharField(max_length=45,default='')
    month12=models.CharField(max_length=45,default='')
    year12=models.CharField(max_length=45,default='')
    RBV_training14=models.CharField(max_length=45,default='')
    month13=models.CharField(max_length=45,default='')
    year13=models.CharField(max_length=45,default='')
    RBV_training15=models.CharField(max_length=45,default='')
    month14=models.CharField(max_length=45,default='')
    year14=models.CharField(max_length=45,default='')
    staff_name=models.ForeignKey(new_staff)

    def __unicode__(self):
         return  self.institution_num1

class employment_history(models.Model):
    institution_num1=models.CharField(max_length=45)
    institution_num2=models.CharField(max_length=45)
    institution_num3=models.CharField(max_length=45)
    position_num1=models.CharField(max_length=45)
    position_num2=models.CharField(max_length=45)
    position_num3=models.CharField(max_length=45)
    start_Date_num1=models.DateField()
    start_Date_num2=models.CharField(max_length=45)
    start_Date_num3=models.CharField(max_length=45)
    end_Date_num1=models.CharField(max_length=45)
    end_Date_num2=models.CharField(max_length=45)
    end_Date_num3=models.CharField(max_length=45)
    responsibilities_num1=models.CharField(max_length=45)
    responsibilities_num2=models.CharField(max_length=45)
    responsibilities_num3=models.CharField(max_length=45)
    staff_name=models.ForeignKey(new_staff)

    def __unicode__(self):
         return  self.institution_num1



class newleave(models.Model):
    first_name = models.CharField(max_length=45)
    last_name =models.CharField(max_length=45)

    department_test=(
        ('GOV', 'GOV'),
        ('ACSD', 'ACSD'),
        ('CSD', 'CSD'),
        ('FISD', 'FISD'),
        ('RSD', 'RSD'),
        ('FMKD', 'FMKD'),
    )
    department=models.CharField(max_length =45, choices=department_test)
    position=models.CharField(max_length =45)

    leavetype=(
        ('Annual', 'Annual'),
       # ('Casual', 'Casual'),
       # ('Sick', 'Sick'),
       # ('Maternity', 'Maternity'),
       # ('Paternity', 'Paternity'),
       # ('Special', 'Special'),
       # ('Study', 'Study'),
       # ('Sabbatical', 'Sabbatical'),
       # ('Compassionate', 'Compassionate'),
    )
    leave_type =models.CharField(max_length=45, choices=leavetype)
    specify_details=models.TextField(default="")
    start_date =models.DateField(null=True)
    end_date=models.DateField(null=True)
    total_working_days=models.FloatField(null=True)

    authorize1=(
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    department_head_authorization =models.CharField(max_length=45,choices = authorize1)
    authorized_by=models.CharField(max_length=45,  default ="")
    remarks=models.TextField()
    authorization_date =models.DateField(null=True)

    authorize2=(
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    Director_authorization =models.CharField(max_length=45, choices=authorize2,null=False)
    Authorization_by=models.CharField(max_length=45, null=False)
    Director_remarks=models.TextField(default ="", null=False)
    Authoriztaion_date =models.DateField(null=True)

    month2=(
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    )
    month=models.CharField(max_length=45, choices =month2,  null=True)
    year =models.CharField(max_length=45, null=True)
    leave_entitlement =models.FloatField(null=True)
    holiday=models.IntegerField(null=True)
    weekend=models.IntegerField(null=True)
    leave_outstanding_balance =models.FloatField(null=True)
    leave_current_balance=models.FloatField(default=0)
    process=(
        ('Processed', 'Processed'),
        ('Revise', 'Revise'),

    )
    process_bal=models.CharField(max_length=45,choices=process,default="")
    username  =models.ForeignKey(User,  default =1)
    staff =models.ForeignKey(new_staff,  default =1)

    def __unicode__(self):
        return self.first_name
