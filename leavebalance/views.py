from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import context,loader
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import  csrf

from models import leavecurrentbalance
from models import staffencashment
from models import uploadfile
from leavebalance.forms import currentleavebalanceform


#from forms import  leave_application
from eLeave.models import  newleave
from eLeave.forms import  leave_application
from leavebalance.forms import staffencashmentform
from leavebalance.forms import update_encashment_form
from leavebalance.forms import uploadfileform
from leavebalance.models import uploadfile
#import csv
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django import template
import djqscsv

import csv

# Create your views here.

def leave_balance(request):
	return render_to_response('leave_balance.html',locals())

def departments(request):
	return render_to_response('govdepartment.html',locals())
#Gov office checking balance
def Gov_aut_check_bal(request):
	return render_to_response('gov_auth_bal_check.html',locals())

#fmkd office current leave balance
def fmkd_currentleave_balance(request):
	return render_to_response('fmkd_leave_balance.html',locals())



def fmd_aut_check_bal(request):
	return render_to_response('fmd_auth_bal_check.html',locals())

#rshd current leave balance
def rshd_currentleave_balance(request):
	return render_to_response('rshd_leave_balance.html',locals())

def rsd_aut_check_bal(request):
	return render_to_response('rsd_auth_bal_check.html',locals())

#acsd current leave balance
def acsd_currentleave_balace(request):
	return render_to_response('acsd_leave_balance.html',locals())

def acsd_aut_check_bal(request):
	return render_to_response('acsd_auth_bal_check.html',locals())

#fisd current leave balance
def fisd_currentleave_balance(request):
	return render_to_response('fisd_leave_balance.html',locals())

def fisd_aut_check_bal(request):
	return render_to_response('fisd_auth_bal_check.html',locals())


#csd current leave balacne
def csd_currentleave_balance(request):
	return render_to_response('csd_leave_balance.html',locals())

def csd_aut_check_bal(request):
	return render_to_response('csd_auth_bal_check.html',locals())

def displaycurrentbalance(request):
	leavebalance=leavecurrentbalance.objects.all()
	return render_to_response('leave_current_balance.html',locals())

#staff balance report
def staffbalance_report(request):
	return render_to_response('staffleavebalance.html')

#department leave balance start
def viewgov_officebalance(request):
	if request.user.username=='sabiut'or request.user.username=='ptari'or request.user.username=='sathy':
		train=leavecurrentbalance.objects.filter(department="GOV")
		return render(request,'govleavebal.html',locals())
	else:
		return render_to_response('hr_redirect.html', {'full_name': request.user.first_name })

def viewfisd_officebalance(request):
	if request.user.username=='sabiut'or request.user.username=='nvari':
		train=leavecurrentbalance.objects.filter(department="FISD")
		return render(request,'fisdleavebal.html',locals())
	else:
		return render_to_response('hr_redirect.html', {'full_name': request.user.first_name })


def viewrsd_officebalance(request):
	if request.user.username=='sabiut'or request.user.username=='gsiri':
		train=leavecurrentbalance.objects.filter(department="RSD")
		return render(request,'rsdleavebal.html',locals())
	else:
		return render_to_response('hr_redirect.html', {'full_name': request.user.first_name })



def viewcsd_officebalance(request):
	if request.user.username=='sabiut'or request.user.username=='nshem':
		train=leavecurrentbalance.objects.filter(department="CSD")
		return render(request,'csdleavebal.html',locals())
	else:
		return render_to_response('hr_redirect.html', {'full_name': request.user.first_name })


def viewacsd_officebalance(request):
	if request.user.username=='sabiut'or request.user.username=='FBeru':
		train=leavecurrentbalance.objects.filter(department="ACSD")
		return render(request,'acsdleavebal.html',locals())
	else:
		return render_to_response('hr_redirect.html', {'full_name': request.user.first_name })

def viewafmd_officebalance(request):
	if request.user.username=='sabiut' or request.user.username=='parubilake':
		train=leavecurrentbalance.objects.filter(department="FMD")
		return render(request,'fmdleavebal.html',locals())
	else:
		return render_to_response('hr_redirect.html', {'full_name': request.user.first_name })

#department leave balance end




#import leave_balance from CSV file
def importleavebalance(request):
	with open('/var/www/projects/webapp/media/currentbalance.csv', 'rb') as csvfile:
		readata=csv.reader(csvfile,delimiter=',',quotechar='"')
		for row in readata:
			if row[0]!='First_Name':
				data=leavecurrentbalance()
				data.First_Name=row[0]
				data.Last_Name=row[1]
				data.Leave_outstanding_balance=row[2]
				data.Monthly_Leave_entitlement=row[3]
				data.Monthly_leave_consumed=row[4]
				data.Total_working_days=row[5]
				data.Year=row[6]
				data.Month=row[7]
				data.Leave_current_balance=row[8]
				data.department=row[9]
				data.leave_encashment=row[10]
				data.save()
		return render_to_response('testsucc.html',locals())


#function to export current leave balance
def download_currentstaffbalance(request):
	csv_export=leavecurrentbalance.objects.values('First_Name','Last_Name','Leave_outstanding_balance','Monthly_Leave_entitlement','Monthly_leave_consumed','Total_working_days','Year','Month','Leave_current_balance','department','leave_encashment')
	return djqscsv.render_to_csv_response(csv_export)


#calculate leave current balance
def leave_balance_calculator(request,id):
	if request.method=='POST':
		a=leavecurrentbalance.objects.get(id=id)
		form=currentleavebalanceform(request.POST,instance=a)
		if form.is_valid():
			balance_current=float(a.Leave_current_balance)
			monthly_leave=float(a.Monthly_leave_consumed)
			total_workday=float(a.Total_working_days)
			a.Monthly_leave_consumed=monthly_leave+total_workday
			currentbalance=balance_current-total_workday
			a.Leave_current_balance=currentbalance
			form.save()
			return render_to_response('current_balancecalculate.html')
	else:
		a=leavecurrentbalance.objects.get(id=id)
		form =currentleavebalanceform(instance=a)
		return render_to_response('view_leave_info.html', {'form': form}, context_instance=RequestContext(request))


#staff view current leave balance
def sum_leavebalance(request):
	if request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Sum ')
		return render_to_response('sum_Abiut_balance.html',locals())

	else:
		return render_to_response('current_balanceredirector.html',locals())


#staff view current leave balance
def sum_leavebalance1(request):
	if request.user.username=='twarsal'or request.user.username=='ptari':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Sum ')
		return render_to_response('gov_office_leave_bal.html',locals())

	else:
		return render_to_response('current_balanceredirector.html',locals())



#leave history
def leavehistory(request):
	if request.user.username=='klunabek':
		leave_log=newleave.objects.filter(first_name='Kalpeau',last_name='Lunabek')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='sabiut':
		leave_log=newleave.objects.filter(first_name='Sum',last_name='Abiut')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='twarsal':
		leave_log=newleave.objects.filter(first_name='Tom',last_name='Warsal')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='tisaiah':
		leave_log=newleave.objects.filter(first_name='Tabe',last_name='Isaiah')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='abaniuri':
		leave_log=newleave.objects.filter(first_name='Alison',last_name='Baniuri')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='ptari':
		leave_log=newleave.objects.filter(first_name='Peter Tari',last_name='Merakali')
		return render_to_response('leave_history.html',locals())

	elif request.user.username=='bkarae':
		leave_log=newleave.objects.filter(first_name='Branan',last_name='Karae')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='amolisa':
		leave_log=newleave.objects.filter(first_name='Andrea Daniella',last_name='Molisa')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='pkalo':
		leave_log=newleave.objects.filter(first_name='Priscilla Salote',last_name='Kalo')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='mhililan':
		leave_log=newleave.objects.filter(first_name='Michael Samuel',last_name='Hililan')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='sathy':
		leave_log=newleave.objects.filter(first_name='Simeon Malachi',last_name='Athy')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='ltarianga':
		leave_log=newleave.objects.filter(first_name='Linnes Moli',last_name='Tarianga')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='mnamak':
		leave_log=newleave.objects.filter(first_name='Malon',last_name='Namak')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='nshem':
		leave_log=newleave.objects.filter(first_name='Nelson Cyrus',last_name='Shem')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='ljonas':
		leave_log=newleave.objects.filter(first_name='Lonneth Dorrah',last_name='Jonas')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='aterry':
		leave_log=newleave.objects.filter(first_name='Alick',last_name='Terry')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='rkaltabau':
		leave_log=newleave.objects.filter(first_name='Rebecca',last_name='Kaltabau')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='kgordon':
		leave_log=newleave.objects.filter(first_name='Keith',last_name='Gordon')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='wpakoa':
		leave_log=newleave.objects.filter(first_name='Willy Saen',last_name='Pakoa')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='akalala':
		leave_log=newleave.objects.filter(first_name='Ambata',last_name='Kalala')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='imarafi':
		leave_log=newleave.objects.filter(first_name='Iven',last_name='Marafi')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='jshem':
		leave_log=newleave.objects.filter(first_name='Joseth',last_name='Shem')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='scharlie':
		leave_log=newleave.objects.filter(first_name='Simeon',last_name='Charlie')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='lgeoffrey':
		leave_log=newleave.objects.filter(first_name='Lillian',last_name='Geoffrey')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='nsarai':
		leave_log=newleave.objects.filter(first_name='Nancy',last_name='Sarai')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='bwilliams':
		leave_log=newleave.objects.filter(first_name='Betty',last_name='William')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='cberu':
		leave_log=newleave.objects.filter(first_name='Charley',last_name='Beru')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='ptagaro':
		leave_log=newleave.objects.filter(first_name='Philip',last_name='Tagaro')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='fkelep':
		leave_log=newleave.objects.filter(first_name='Fred',last_name='Kelep')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='tnawinmal':
		leave_log=newleave.objects.filter(first_name='Thevfa',last_name='Nawinmal')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='nmagau':
		leave_log=newleave.objects.filter(first_name='Nauni',last_name='Magau')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='fneimei':
		leave_log=newleave.objects.filter(first_name='Fred Ellie',last_name='Neimei')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='gkalmet':
		leave_log=newleave.objects.filter(first_name='Gengis Khan',last_name='Kalmet')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='dsiro':
		leave_log=newleave.objects.filter(first_name='Daffodil',last_name='Siro')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='jjohn':
		leave_log=newleave.objects.filter(first_name='Jessica Leitau',last_name='John')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='ajohn':
		leave_log=newleave.objects.filter(first_name='Aaron',last_name='John')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='faru':
		leave_log=newleave.objects.filter(first_name='Florinda',last_name='Aru')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='rkaltonga':
		leave_log=newleave.objects.filter(first_name='Ruth',last_name='Kaltonga')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='jiauma':
		leave_log=newleave.objects.filter(first_name='Julia',last_name='Iauma')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='clendal':
		leave_log=newleave.objects.filter(first_name='Carolyn',last_name='Lendal')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='kseri':
		leave_log=newleave.objects.filter(first_name='Kensen Tabi',last_name='Seri')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='pmalites':
		leave_log=newleave.objects.filter(first_name='Pedro Benneth',last_name='Malites')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='jvira':
		leave_log=newleave.objects.filter(first_name='Juanita',last_name='Vira')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='smarum':
		leave_log=newleave.objects.filter(first_name='Sereana',last_name='Marum')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='sthomas':
		leave_log=newleave.objects.filter(first_name='Shirley',last_name='Thomas')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='kloumai':
		leave_log=newleave.objects.filter(first_name='Kenny',last_name='Loumai')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='halilee':
		leave_log=newleave.objects.filter(first_name='Heva',last_name='Alilee')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='kkaltabang':
		leave_log=newleave.objects.filter(first_name='Kasea',last_name='Kaltabang')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='llesly':
		leave_log=newleave.objects.filter(first_name='Leinasei',last_name='Lesly')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='skarlyp':
		leave_log=newleave.objects.filter(first_name='Semu',last_name='Karlyp')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='sjoshua':
		leave_log=newleave.objects.filter(first_name='Suzy',last_name='Joshua')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='ndaniel':
		leave_log=newleave.objects.filter(first_name='Nerry',last_name='Daniel')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='dalexander':
		leave_log=newleave.objects.filter(first_name='Derek',last_name='Alexander')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='mnixon':
		leave_log=newleave.objects.filter(first_name='Melonnie Nixon',last_name='Lester')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='chaggai':
		leave_log=newleave.objects.filter(first_name='Cynthia Rona',last_name='Haggai')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='gsiri':
		leave_log=newleave.objects.filter(first_name='Gloria',last_name='Siri')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='akaltongga':
		leave_log=newleave.objects.filter(first_name='Alumeci',last_name='Kaltongga')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='ptoa':
		leave_log=newleave.objects.filter(first_name='Pita',last_name='Toa')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='ldaniel':
		leave_log=newleave.objects.filter(first_name='Linda',last_name='Daniel')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='cala':
		leave_log=newleave.objects.filter(first_name='Cynthia',last_name='Moli')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='abill':
		leave_log=newleave.objects.filter(first_name='Arold',last_name='Bill')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='fvinabit':
		leave_log=newleave.objects.filter(first_name='Fabiano',last_name='Vinabit')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='rpeter':
		leave_log=newleave.objects.filter(first_name='Robert',last_name='Peter')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='lragonmal':
		leave_log=newleave.objects.filter(first_name='Lynette',last_name='Ragonmal')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='jwillie':
		leave_log=newleave.objects.filter(first_name='Joylin Lydia',last_name='Willie')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='mtamata':
		leave_log=newleave.objects.filter(first_name='Mark Ala',last_name='Tamata')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='parubilake':
		leave_log=newleave.objects.filter(first_name='Philip',last_name='Arubilake')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='lstephens':
		leave_log=newleave.objects.filter(first_name='Lynrose',last_name='Stephens')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='stiwok':
		leave_log=newleave.objects.filter(first_name='Simon',last_name='Tiwok')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='fjacob':
		leave_log=newleave.objects.filter(first_name='Fredrick',last_name='Jacob')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='vbarang':
		leave_log=newleave.objects.filter(first_name='Victoria',last_name='Barang')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='tgarae':
		leave_log=newleave.objects.filter(first_name='Tonny',last_name='Garae')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='abena':
		leave_log=newleave.objects.filter(first_name='Albert',last_name='Bena')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='jmalasikoto':
		leave_log=newleave.objects.filter(first_name='Juliana',last_name='Malasikoto')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='jbebe':
		leave_log=newleave.objects.filter(first_name='Johncy Waimer',last_name='Bebe')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='nvari':
		leave_log=newleave.objects.filter(first_name='Noel',last_name='Vari')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='jewillie':
		leave_log=newleave.objects.filter(first_name='Jenny',last_name='Willie')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='fkalorib':
		leave_log=newleave.objects.filter(first_name='Florida',last_name='Kalorib')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='hbule':
		leave_log=newleave.objects.filter(first_name='Holyoke',last_name='Bule')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='mmera':
		leave_log=newleave.objects.filter(first_name='Mark Colin',last_name='Mera')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='jtabiusu':
		leave_log=newleave.objects.filter(first_name='John Liu',last_name='Tabiusu')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='nmabon':
		leave_log=newleave.objects.filter(first_name='Nancy Fay',last_name='Mabon')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='aralph':
		leave_log=newleave.objects.filter(first_name='Alex',last_name='Bisiwei')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='mabbil':
		leave_log=newleave.objects.filter(first_name='Marinette Lucy',last_name='Abbil')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='nwoi':
		leave_log=newleave.objects.filter(first_name='Noelyne Woi',last_name='Viro')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='mkaltapiri':
		leave_log=newleave.objects.filter(first_name='Mesek',last_name='Kaltapiri')
		return render_to_response('leave_history.html',locals())
	elif request.user.username=='gmassing':
		leave_log=newleave.objects.filter(first_name='Glenda',last_name='Massing')
		return render_to_response('leave_history.html',locals())

	else:


	   	 return render_to_response('current_balanceredirector.html',locals())

#download leave History
def download_history(request):
	csv_export=newleave.objects.filter(first_name="sum",last_name="Abiut")
	return djqscsv.render_to_csv_response(csv_export)



def kalpeau_leavebalance(request):
	if request.user.username=='klunabek':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Kalpeau')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


def kalpeau_leavebalance1(request):
	if request.user.username=='ptari'or request.user.username=='sathy':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Kalpeau')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())




#Tabe Isaiah current leave balance
def Tabe_leavebalance(request):
	if request.user.username=='tisaiah':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Isaiah')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Tabe Isaiah current leave balance
def Tabe_leavebalance1(request):
	if request.user.username=='twarsal' or request.user.username=='ptari':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Isaiah')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Tom Warsal current leave balance
def Tom_leavebalance(request):
	if request.user.username=='twarsal':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Warsal')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Tom Warsal current leave balance
def Tom_leavebalance1(request):
	if request.user.username=='ptari' or request.user.username=='sathy':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Warsal')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())



#Simeon Athy  current leave balance
def Governor_leavebalance(request):
	if request.user.username=='sathy':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='M. Athy')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Simeon Athy  current leave balance
def Governor_leavebalance1(request):
	if request.user.username=='ptari':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='M. Athy')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Peter Tari  current leave balance
def deputyGovernor_leavebalance(request):
	if request.user.username=='ptari':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Merakali')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())



#Peter Tari  current leave balance
def deputyGovernor_leavebalance1(request):
	if request.user.username=='sathy':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='T. Merakali')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())



#Michael hililan  current leave balance
def Michael_leavebalance(request):
	if request.user.username=='mhililan':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Hililan')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


def Michael_leavebalance1(request):
	if request.user.username=='sathy' or request.user.username=='ptari':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Hililan')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Linnes  current leave balance
def Linnes_leavebalance(request):
	if request.user.username=='ltarianga':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Tarianga ')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Linnes  current leave balance
def Linnes_leavebalance1(request):
	if request.user.username=='sathy' or request.user.username=='ptari':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Tarianga ')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())



#George  current leave balance
def George_leavebalance(request):
	if request.user.username=='gtasso':
		sum_currentbalance=leavecurrentbalance.objects.filter(First_Name='George ', Last_Name='Tasso')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Branan current leave balance
def Branan_leavebalance(request):
	if request.user.username=='bkarae':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Branan ')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Branan current leave balance
def Branan_leavebalance1(request):
	if request.user.username=='sathy' or request.user.username=='ptari':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Branan ')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Andrea current leave balance
def andrea_leavebalance(request):
	if request.user.username=='amolisa':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Molisa ')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Andrea current leave balance
def andrea_leavebalance1(request):
	if request.user.username=='klunabek'or request.user.username=='ptari':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Molisa ')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Pricilla current leave balance
def Priscilla_leavebalance(request):
	if request.user.username=='pkalo':
		sum_currentbalance=leavecurrentbalance.objects.filter(First_Name='Priscilla Salote')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Pricilla current leave balance
def Priscilla_leavebalance1(request):
	if request.user.username=='twarsal'or request.user.username=='ptari':
		sum_currentbalance=leavecurrentbalance.objects.filter(First_Name='Priscilla Salote')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Malon current leave balance
def Malon_leavebalance(request):
	if request.user.username=='mnamak':
		sum_currentbalance=leavecurrentbalance.objects.filter(First_Name='Malon ')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Malon current leave balance
def Malon_leavebalance1(request):
	if request.user.username=='twarsal'or request.user.username=='ptari':
		sum_currentbalance=leavecurrentbalance.objects.filter(First_Name='Malon ')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())




#FMKD Leave Balance
#Albert current leave balance
def Albert_leavebalance(request):
	if request.user.username=='abena' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Bena')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Albert current leave balance
def Albert_leavebalance1(request):
	if request.user.username=='parubilake' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Bena')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())




#Alison current leave balance
def Alison_leavebalance(request):
	if request.user.username=='abaniuri'or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Baniuri')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Alison current leave balance
def Alison_leavebalance1(request):
	if request.user.username=='ptari' or request.user.username=='sabiut' or request.user.username=='sathy':
		sum_currentbalance=leavecurrentbalance.objects.filter(First_Name='Baniuri')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Frederic Jacob current leave balance
def Frederic_leavebalance(request):
	if request.user.username=='fjacob' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter(First_Name='Frederick')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


def Frederic_leavebalance1(request):
	if request.user.username=='parubilake'or request.user.username=='lstephens':
		sum_currentbalance=leavecurrentbalance.objects.filter(First_Name='Frederick')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Johncy Bebecurrent leave balance
def Johncy_leavebalance(request):
	if request.user.username=='jbebe' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Bebe')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Johncy Bebecurrent leave balance
def Johncy_leavebalance1(request):
	if request.user.username=='parubilake':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Bebe')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())



#Lynrose Stephens current leave balance
def Lynrose_leavebalance(request):
	if request.user.username=='lstephens' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Stephens')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


def Lynrose_leavebalance1(request):
	if request.user.username=='parubilake':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Stephens')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Philip Arubilake  current leave balance
def philip_leavebalance(request):
	if request.user.username=='parubilake' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Arubilake ')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Philip Arubilake  current leave balance
def philip_leavebalance1(request):
	if request.user.username=='sathy'or request.user.username=='ptari':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Arubilake ')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Robinsion Tomniavia  current leave balance
def robinsion_leavebalance(request):
	if request.user.username=='rtomniavia':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Robinsion', Last_Name='Tomniavia')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Simon Tiwok  current leave balance
def Simon_leavebalance(request):
	if request.user.username=='stiwok':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='simon', Last_Name='tiwok')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Tonny Garae  current leave balance
def Tonny_leavebalance(request):
	if request.user.username=='tgarae' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Garae')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


def Tonny_leavebalance1(request):
	if request.user.username=='lstephens' or request.user.username=='parubilake':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Garae')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Vicky Barang  current leave balance
def Vicky_leavebalance(request):
	if request.user.username=='vbarang' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Barang')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Vicky Barang  current leave balance
def Vicky_leavebalance1(request):
	if request.user.username=='parubilake'or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Barang')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Juliana Malasikoto  current leave balance
def Juliana_leavebalance(request):
	if request.user.username=='jmalasikoto' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Malasikoto')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Juliana Malasikoto   current leave balance
def Juliana_leavebalance1(request):
	if request.user.username=='parubilake'or request.user.username=='sabiut' or request.user.username=='lstephens':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Malasikoto')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#CSD Leave Balance
#Alick Terry current leave balance
def Alick_leavebalance(request):
	if request.user.username=='aterry' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Alick')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


def Alick_leavebalance1(request):
	if request.user.username=='nshem':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Alick')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())



#Ambata Jimmy  current leave balance
def Ambata_leavebalance(request):
	if request.user.username=='akalala' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Ambata ')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Ambata Jimmy  current leave balance
def Ambata_leavebalance1(request):
	if request.user.username=='nshem'or request.user.username=='aterry':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Ambata ')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Betty Williams  current leave balance
def Betty_leavebalance(request):
	if request.user.username=='bwilliams' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Williams')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Betty Williams  current leave balance
def Betty_leavebalance1(request):
	if request.user.username=='nshem' or request.user.username=='aterry':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Williams')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Charlie Simeon  current leave balance
def Charlie_leavebalance(request):
	if request.user.username=='csimeon' or  request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Charlie')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Charlie Simeon  current leave balance
def Charlie_leavebalance1(request):
	if request.user.username=='nshem' or  request.user.username=='ljonas':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Charlie')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Charlie Beru  current leave balance
def CharlieBeru_leavebalance(request):
	if request.user.username=='cberu'or  request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Beru')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Charlie Beru  current leave balance
def CharlieBeru_leavebalance1(request):
	if request.user.username=='nshem'or  request.user.username=='aterry':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Beru')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Daffodil Daruhi  current leave balance
def Daffodil_leavebalance(request):
	if request.user.username=='dsiro'or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Daffodil')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Daffodil Daruhi  current leave balance
def Daffodil_leavebalance1(request):
	if request.user.username=='aterry' or request.user.username=='nshem':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Daffodil')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Fred celeb  current leave balance
def Fred_leavebalance(request):
	if request.user.username=='fkelep'or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Fred ')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Fred_leavebalance1(request):
	if request.user.username=='aterry' or request.user.username=='nshm':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Fred ')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Iven Marafi  current leave balance
def Iven_leavebalance(request):
	if request.user.username=='imarafi' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Marafi')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Iven Marafi  current leave balance
def Iven_leavebalance1(request):
	if request.user.username=='nshem' or request.user.username=='ljonas':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Marafi')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Jessica John   current leave balance
def Jessica_leavebalance(request):
	if request.user.username=='jjohn'or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Jessica Leitau')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Jessica John   current leave balance
def Jessica_leavebalance1(request):
	if request.user.username=='nshem':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Jessica Leitau')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Joseth Shem  current leave balance
def Joseth_leavebalance(request):
	if request.user.username=='jshem'or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Joseth ')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


def Joseth_leavebalance1(request):
	if request.user.username=='nshem'or request.user.username=='aterry':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Joseth ')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Keith Gordon current leave balance
def keith_leavebalance(request):
	if request.user.username=='kgordon'or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Keith')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def keith_leavebalance1(request):
	if request.user.username=='aterry' or request.user.username=='nshem':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Keith')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Ken Kalmet  current leave balance
def ken_leavebalance(request):
	if request.user.username=='kkalmet':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Gengis')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


def ken_leavebalance1(request):
	if request.user.username=='aterry' or request.user.username=='nshem':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Gengis')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Lonneth Jonas  current leave balance
def Lonneth_leavebalance(request):
	if request.user.username=='ljonas' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Jonas')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


def Lonneth_leavebalance1(request):
	if request.user.username=='nshem':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Jonas')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Lillian Jeffrey current leave balance
def Lillian_leavebalance(request):
	if request.user.username=='ljeffery' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Geoffrey')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


def Lillian_leavebalance1(request):
	if request.user.username=='nshem' or request.user.username=='aterry':
		sum_currentbalance=leavecurrentbalance.objects.filter(First_Name='Geoffrey')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Nelson Shem  current leave balance
def Nelson_leavebalance(request):
	if request.user.username=='nshem'or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Nelson ')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Nelson_leavebalance1(request):
	if request.user.username=='ptari' or request.user.username=='sathy':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Nelson ')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())



#Nancy Sarai  current leave balance
def Nancys_leavebalance(request):
	if request.user.username=='nsarai'or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Sarai')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Nancys_leavebalance1(request):
	if request.user.username=='nshem' or request.user.username=='aterry':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Sarai')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())



#Pakoa Nissu  current leave balance
def Pakoa_leavebalance(request):
	if request.user.username=='pnissu' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Willy ')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Pakoa_leavebalance1(request):
	if request.user.username=='aterry'or request.user.username=='nshem':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Willy ')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Philip Tagaro  current leave balance
def Philip_leavebalance(request):
	if request.user.username=='ptagar' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Philip')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


def Philip_leavebalance1(request):
	if request.user.username=='nshem' or request.user.username=='aterry':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Philip')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Rebecca Bakeo current leave balance
def Rebeca_leavebalance(request):
	if request.user.username=='rbakeo' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Rebecca')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Rebeca_leavebalance1(request):
	if request.user.username=='nshem' or request.user.username=='aterry':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Rebecca')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Thevfa Nawinmal  current leave balance
def Thevfa_leavebalance(request):
	if request.user.username=='tnawinmal' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Thevfa')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Thevfa_leavebalance1(request):
	if request.user.username=='aterry' or request.user.username=='nshem':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Thevfa')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Nauni Magau leave balance
def Nauni_leavebalance(request):
	if request.user.username=='nmagau' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Nauni')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Nauni_leavebalance1(request):
	if request.user.username=='aterry' or request.user.username=='nshem':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Nauni')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Ellie leave balance
def Ellie_leavebalance(request):
	if request.user.username=='fneimei' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter(First_Name='Fred Ellie ')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Ellie_leavebalance1(request):
	if request.user.username=='aterry' or request.user.username=='nshem':
		sum_currentbalance=leavecurrentbalance.objects.filter(First_Name='Fred Ellie ')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Ellie leave balance
def Aaron_leavebalance(request):
	if request.user.username=='ajohn' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Aaron Gideon')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Aaron_leavebalance1(request):
	if request.user.username=='aterry' or request.user.username=='nshem':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Aaron Gideon')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Glenda Massing
def Glenda_leavebalance(request):
	if request.user.username=='gmassing' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Glenda')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Glenda_leavebalance1(request):
	if request.user.username=='aterry' or request.user.username=='nshem':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Glenda')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())





 #ACSD																																																																																																								ACSD Leave balance
#Beneth Malites  current leave balance
def Beneth_leavebalance(request):
	if request.user.username=='bmalites' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Malites')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Beneth Malites  current leave balance
def Beneth_leavebalance1(request):
	if request.user.username=='faru':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Malites')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())



#Mesek  current leave balance
def Mesek_leavebalance(request):
	if request.user.username=='mkaltapiri' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Kaltapiri')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Mesek current leave balance
def Mesek_leavebalance1(request):
	if request.user.username=='faru':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Kaltapiri')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())





#Carolyn Lendal current leave balance
def Carolyn_leavebalance(request):
	if request.user.username=='clendal' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Lendal')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Carolyn Lendal current leave balance
def Carolyn_leavebalance1(request):
	if request.user.username=='faru':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Lendal')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())



#Derek Alexander  current leave balance
def Derek_leavebalance(request):
	if request.user.username=='dalexander' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Alexander')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Derek_leavebalance1(request):
	if request.user.username=='faru':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Alexander')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Florinda Beru current leave balance
def Florinda_leavebalance(request):
	if request.user.username=='faru' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Aru')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Florinda_leavebalance1(request):
	if request.user.username=='sabiut' or request.user.username=='ptari':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Aru')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Juanita Vira  current leave balance
def Juanita_leavebalance(request):
	if request.user.username=='jvira' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Juanita')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Juanita_leavebalance1(request):
	if request.user.username=='faru':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Juanita')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Julia Lauma  current leave balance
def Julia_leavebalance(request):
	if request.user.username=='jiauma' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Iauma')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Julia_leavebalance1(request):
	if request.user.username=='kseri' or request.user.username=='faru':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Iauma')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Keny Loumai  current leave balance
def Kenny_leavebalance(request):
	if request.user.username=='kloumai'or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Kenny')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Kenny_leavebalance1(request):
	if request.user.username=='kseri' or request.user.username=='faru':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Kenny')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Kensen Seri  current leave balance
def Kensen_leavebalance(request):
	if request.user.username=='kseri' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Seri')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Kensen_leavebalance1(request):
	if request.user.username=='faru':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Seri')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Ruth Kaltonga  current leave balance
def Ruth_leavebalance(request):
	if request.user.username=='rkaltonga' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Ruth')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Ruth_leavebalance1(request):
	if request.user.username=='smarum' or request.user.username=='faru':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Ruth')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Sussie Joshua  current leave balance
def Sussie_leavebalance(request):
	if request.user.username=='sjoshua' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Joshua')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Sussie_leavebalance1(request):
	if request.user.username=='kseri' or request.user.username=='faru':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Joshua')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Shirly Thomas  current leave balance
def Shirly_leavebalance(request):
	if request.user.username=='sthomas' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Shirley ')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Shirly_leavebalance1(request):
	if request.user.username=='smarum' or request.user.username=='faru':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Shirley ')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Currency  leave balance

#Heva current leave balance
def heva_leavebalance(request):
	if request.user.username=='halilee' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Heva')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def heva_leavebalance1(request):
	if request.user.username=='faru':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Heva')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Melonnie current leave balance
def Melonnie_leavebalance(request):
	if request.user.username=='mnixon' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Lester')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Melonnie_leavebalance1(request):
	if request.user.username=='faru'or request.user.username=='halilee':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Lester')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())



#Semu current leave balance
def Semu_leavebalance(request):
	if request.user.username=='skarlyp' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Semu ')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def semu_leavebalance1(request):
	if request.user.username=='faru'or request.user.username=='halilee':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Semu ')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Kasaia current leave balance
def Kasaia_leavebalance(request):
	if request.user.username=='kkaltabang' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Kaltabang')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Kasaia_leavebalance1(request):
	if request.user.username=='faru'or request.user.username=='halilee':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Kaltabang')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Leinasei current leave balance
def Leinasei_leavebalance(request):
	if request.user.username=='landerson' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Leinasei')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Leinasei_leavebalance1(request):
	if request.user.username=='faru'or request.user.username=='halilee':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Leinasei')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Haggai current leave balance
def	Haggai_leavebalance(request):
	if request.user.username=='chaggai' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Haggai')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Haggai_leavebalance1(request):
	if request.user.username=='faru'or request.user.username=='halilee':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Haggai')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Sereana current leave balance
def	Sereana_leavebalance(request):
	if request.user.username=='smarum' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Marum')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Sereana_leavebalance1(request):
	if request.user.username=='faru':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Marum')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Nerry current leave balance
def	Nerry_leavebalance(request):
	if request.user.username=='ndaniel' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Nerry ')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Nerry_leavebalance1(request):
	if request.user.username=='faru':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Nerry ')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())








#RSHD leave Balance
#Alumeci Kaltongga  current leave balance
def Alumeci_leavebalance(request):
	if request.user.username=='akaltongga' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Alumeci')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Alumeci_leavebalance1(request):
	if request.user.username=='gsiri':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Alumeci')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Arnold Bill current leave balance
def Arnold_leavebalance(request):
	if request.user.username=='abill' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Bill')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Arnold_leavebalance1(request):
	if request.user.username=='gsiri'or request.user.username=='lragonmal':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Bill')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Cynthia Ala Moli  current leave balance
def cynthia_leavebalance(request):
	if request.user.username=='cala' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Moli')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def cynthia_leavebalance1(request):
	if request.user.username=='gsiri':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Moli')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Fabiano Vinabit  current leave balance
def Fabiano_leavebalance(request):
	if request.user.username=='fvinabit' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Fabiano')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Fabiano_leavebalance1(request):
	if request.user.username=='gsiri' or request.user.username=='cala':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Fabiano')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Jerry Niatu   current leave balance
def Jerry_leavebalance(request):
	if request.user.username=='jniatu' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Jerry ')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Jerry_leavebalance1(request):
	if request.user.username=='jniatu': #Who approves leave (name not in list)
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Jerry ')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Joyline Willie  current leave balance
def Joyin_leavebalance(request):
	if request.user.username=='jbwillie' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Joylin Willie')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Joyin_leavebalance1(request):
	if request.user.username=='gsiri' or request.user.username=='akaltongga':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Joylin Willie')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Linda Daniel  current leave balance
def Linda_leavebalance(request):
	if request.user.username=='ldaniel' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Malesie ')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Linda_leavebalance1(request):
	if request.user.username=='gsiri':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Malesie ')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Mark Tamata  current leave balance
def Mark_leavebalance(request):
	if request.user.username=='mtamata' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Tamata')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Mark_leavebalance1(request):
	if request.user.username=='gsiri':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Tamata')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Pita Toa   current leave balance
def Pita_leavebalance(request):
	if request.user.username=='ptoa' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Toa')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Pita_leavebalance1(request):
	if request.user.username=='gsiri':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Toa')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Robert Peter  current leave balance
def Robert_leavebalance(request):
	if request.user.username=='rpeter' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Robert ')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Robert_leavebalance1(request):
	if request.user.username=='gsiri' or request.user.username=='cala':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Robert ')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Lynette current leave balance
def Lynette_leavebalance(request):
	if request.user.username=='lragonmal' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Ragonmal')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Lynette_leavebalance1(request):
	if request.user.username=='gsiri': #no name on list
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Ragonmal')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#FISD Leave Balance
#Alex Bisiwel current leave balance
def Alex_leavebalance(request):
	if request.user.username=='aralph' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Alex Maru')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Alex_leavebalance1(request):
	if request.user.username=='mmera' or request.user.username=='nvari':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Alex Maru')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Florida Kalorib current leave balance
def Florinda_leavebalancefisd(request):
	if request.user.username=='fkalorib'or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Philip')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Florinda_leavebalancefisd1(request):
	if request.user.username=='mmera' or request.user.username=='nvari':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Philip')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Gloria Seri current leave balance
def Gloria_leavebalance(request):
	if request.user.username=='gseri' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Gloria')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Gloria_leavebalance1(request):
	if request.user.username=='sathy' or request.user.username=='ptari':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Gloria')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Holyoake Bule current leave balance
def Holyoake_leavebalance(request):
	if request.user.username=='hbule' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Holyoake ')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Holyoake_leavebalance1(request):
	if request.user.username=='mabbil' or request.user.username=='nvari':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Holyoake ')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())



#John Tabiusu current leave balance
def John_leavebalance(request):
	if request.user.username=='jtabiusu' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='John Lui')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def John_leavebalance1(request):
	if request.user.username=='nvari':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='John Lui')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Jenny Willie current leave balance
def Jenny_leavebalance(request):
	if request.user.username=='jwillie' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Jenny')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Jenny_leavebalance1(request):
	if request.user.username=='nvari':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Jenny')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Marinet Abbil current leave balance
def Marinet_leavebalance(request):
	if request.user.username=='mabbil' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Abbil')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Marinet_leavebalance1(request):
	if request.user.username=='nvari':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Abbil')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Mark Mera current leave balance
def MMark_leavebalance(request):
	if request.user.username=='mmera' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Mera')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def MMark_leavebalance1(request):
	if request.user.username=='nvari':
		sum_currentbalance=leavecurrentbalance.objects.filter(Last_Name='Mera')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Nancy Mabon current leave balance
def Nancy_leavebalance(request):
	if request.user.username=='nmabon' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Mabon')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Nancy_leavebalance1(request):
	if request.user.username=='nvari':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Mabon')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())


#Noel Vari current leave balance
def Noel_leavebalance(request):
	if request.user.username=='nvari' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Noel ')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Noel_leavebalance1(request):
	if request.user.username=='sathy' or request.user.username=='ptari':
		sum_currentbalance=leavecurrentbalance.objects.filter( First_Name='Noel ')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

#Noelyne Woi current leave balance
def Noelyn_leavebalance(request):
	if request.user.username=='nwoi' or request.user.username=='sabiut':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Viro')
		return render_to_response('sum_Abiut_balance.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())

def Noelyn_leavebalance1(request):
	if request.user.username=='mabbil' or request.user.username=='nvari':
		sum_currentbalance=leavecurrentbalance.objects.filter( Last_Name='Viro')
		return render_to_response('gov_office_leave_bal.html',locals())
	else:
		return render_to_response('current_balanceredirector.html',locals())



#staff encashment page
#def encash(reequest):
	#if request.user.username=='klunabek'or request.user.username=='sabiut'or request.user.username=='kseri' or request.user.username=='kloumai' or request.user.username=='jiauma':
		#return render_to_response('accounts.html',{'full_name': request.user.first_name},context_instance=RequestContext(request))
	#else:
		#return render_to_response('hr_redirect.html', {'full_name': request.user.first_name })


def encash(request):
    if request.user.username=='sabiut' or request.user.username=='kseri' or request.user.username=='kloumai' or request.user.username=='jiauma':
        return render_to_response('accounts.html', locals())
    else:
        return render_to_response('leave_authorizor_redirector.html', {'full_name': request.user.first_name })


#staff encashment

#def encashment(request):
	#if request.POST:
		#form =staffencashmentform(request.POST)
		#if form.is_valid():
			#form.save()
			#return render_to_response('click_for_authorization.html')
		#else:
			#form=staffencashmentform
		#args={}
		#args.update(csrf(request))
		#return render_to_response('encashment_form.html',args)


def encashment(request):
    if request.POST:
        form =staffencashmentform(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('successful_encashment.html')
    else:
        form =staffencashmentform
    args={}
    args.update(csrf(request))
    args['form']=form
    return render_to_response('encashment_form.html', args)


def encashment_display(request):
	encash=staffencashment.objects.all()
	return render_to_response('encashment_views.html',locals())

def leave_payout(request):
	encash=staffencashment.objects.all()
	return render_to_response('hr_encashment.html',locals())

def accounts(request):
	leaveencash=leavecurrentbalance.objects.all()
	return render_to_response('accounts_update_encashment.html',locals())


def leave_encashment_calculator(request,id):
	if request.method=='POST':
		a=leavecurrentbalance.objects.get(id=id)
		form=update_encashment_form(request.POST,instance=a)
		if form.is_valid():
			leave_encashment=float(a.leave_encashment)
			current_balance=float(a.Leave_current_balance)
			#balance=float(a.Leave_current_balance)-float(a.Leave_current_balance)
			balance=current_balance-leave_encashment
			a.Leave_current_balance=balance
			form.save()
			return render_to_response('successful_encashment.html')
	else:
		a=leavecurrentbalance.objects.get(id=id)
		form =update_encashment_form(instance=a)
		return render_to_response('view_staff_encashment.html', {'form': form}, context_instance=RequestContext(request))




#upload files
def uploadfunc(request):
	if request.method=='POST':
		form =uploadfileform(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response('upload_successful.html')
	else:
		form=uploadfileform()
	return render(request, 'upload.html',{'form':form})

def displayfile(request):
	documents = uploadfile.objects.all()
	documents.delete()
	return render_to_response('disfile.html')
