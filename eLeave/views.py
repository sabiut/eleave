from django.shortcuts import render, redirect,  get_object_or_404
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context, loader
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import  auth
from django.core.context_processors import  csrf
import operator
from forms import  leave_application
from forms import  leaveapplication2
from forms import authoriseleave
from forms import  addstaff
from forms import coporateservices_authoriseleave
from forms import leavecalculator
from forms import train
from forms import institution
from forms import processbalanceform
#from models import staff
#from models import leave
from models import  newleave
from models import new_staff
from models import training
from models import employment_history
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django import template

#export file to csv
import djqscsv

# Create your views here.

def index(request):
   # return HttpResponse('welcome to ELeave App')
    c ={}
    c.update(csrf(request))
    return render_to_response('index.html', c)

def auth_view(request):
        username=request.POST.get('username', '')
        password=request.POST.get('password', '')
        user =auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/eLeave/loggedin')
        else:
            return HttpResponseRedirect('/eLeave/invalid')

def loggedin(request):
    return render_to_response('loggedin.html', {'full_name': request.user.first_name})

def invalid(request):
    return render_to_response('invalid.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')



def leaves(request):
    if request.POST:
        form =leaveform(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response("Record was added successfully")
    else:
        form =leaveform
    args={}
    args.update(csrf(request))
    args['form']=form
    return render_to_response('leaves.html', args)


def edit_staff(request):
    if request.POST:
        form =editstaff(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response("successful.html")
    else:
        form =editstaff
    args={}
    args.update(csrf(request))
    args['form']=form
    return render_to_response('edit_staff.html', args)

#leave application form
def leaveapplication(request):
    if request.POST:
        form =leave_application(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('click_for_authorization.html')
    else:
        form =leave_application
    args={}
    args.update(csrf(request))
    args['form']=form
    return render_to_response('newleave_application.html', args)


#leave application form 2
def leave_application2(request):
    if request.POST:
        form =leaveapplication2(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response("successful.html")
    else:
        form =leaveapplication2
    args={}
    args.update(csrf(request))
    args['form']=form
    return render_to_response('newleave_application2.html', args)


#adding new staff form
def newstaff(request):
    if request.POST:
        form =addstaff(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response("successful.html")
    else:
        form =addstaff
    args={}
    args.update(csrf(request))
    args['form']=form
    return render_to_response('addnewstaff.html', args)


def training_edu(request):
    if request.POST:
        form =train(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response("successful1.html")
    else:
        form =train
    args={}
    args.update(csrf(request))
    args['form']=form
    return render_to_response('training.html', args)

def institution_name(request):
    if request.POST:
        form =institution(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response("successful2.html")
    else:
        form =institution
    args={}
    args.update(csrf(request))
    args['form']=form
    return render_to_response('institution.html', args)



def display_view(request):
     #return render_to_response('display.html')
    staffs=staff.objects.select_related()
    #leaves=leave.objects.all()
    return render_to_response('display.html', locals(),  context_instance=RequestContext(request))

#display Staff info
def dispay_staff(request):
    staffs=new_staff.objects.all()
    return render_to_response('display_staffinfo.html', locals())

#display Staff training history
def dispay_staff_training(request):
    training_his= training.objects.all()
    return render_to_response('display_stafftraining.html', locals())

#display Staff employment history
def dispay_staff_employment(request):
    employment_his= employment_history.objects.all()
    return render_to_response('display_staffemployment.html', locals())

#display RBV training history
def dispay_rbv_training(request):
    rbvtraining= training.objects.all()
    return render_to_response('rbv_training.html', locals())

#edit staff information
def edit_staffinfo(request, id):
    if request.method == 'POST':
        a=new_staff.objects.get(id=id)
        form = addstaff(request.POST, instance=a)
        if form.is_valid():
            form.save()
            return render_to_response('save_edited_staff.html')
    else:
        a=new_staff.objects.get(id=id)
        form =  addstaff(instance=a)
        return render_to_response('staffinfo_edit.html', {'form': form}, context_instance=RequestContext(request))

#edit staff Training
def edit_stafftraining(request, id):
    if request.method == 'POST':
        a=training.objects.get(id=id)
        form = train(request.POST, instance=a)
        if form.is_valid():
            form.save()
            return render_to_response('save_edited_training.html')
    else:
        a= training.objects.get(id=id)
        form =  train(instance=a)
        return render_to_response('stafftraining_edit.html', {'form': form}, context_instance=RequestContext(request))

#edit staff employment history
def edit_staffemployment(request, id):
    if request.method == 'POST':
        a=employment_history.objects.get(id=id)
        form =institution(request.POST, instance=a)
        if form.is_valid():
            form.save()
            return render_to_response('save_edited_training.html')
    else:
        a= employment_history.objects.get(id=id)
        form =  institution(instance=a)
        return render_to_response('staffemployment_edit.html', {'form': form}, context_instance=RequestContext(request))

#display leave info
def leave_info(request):
    new_leave=newleave.objects.all()
    return render_to_response('display_newleave.html', locals())

 #Display list of leave application for authorazation for each department by department head
def leave_to_authorize(request):
    new_leave=newleave.objects.filter(department="GOV")
    return render_to_response('GOV_display_approve_leave.html', locals())

def FMKD_leave_to_authorize(request):
    new_leave=newleave.objects.filter(department="FMKD")
    return render_to_response('FMKD_display_approve_leave.html', locals())

def CSD_leave_to_authorize(request):
    new_leave=newleave.objects.filter(department="CSD")
    return render_to_response('CSD_display_approve_leave.html', locals())

def ACSD_leave_to_authorize(request):
    new_leave=newleave.objects.filter(department="ACSD")
    return render_to_response('ACSD_display_approve_leave.html', locals())

def RSHD_leave_to_authorize(request):
    new_leave=newleave.objects.filter(department="RSHD")
    return render_to_response('RSHD_display_approve_leave.html', locals())

def FISD_leave_to_authorize(request):
    new_leave=newleave.objects.filter(department="FISD")
    return render_to_response('FISD_display_approve_leave.html', locals())

        #-------Department Head End------#


#coporate services to approve leave
def coporateservices_authorization(request):
    return render_to_response('coporate_services_to_approve_leave.html')


#Display coporate services authorization
def coporate_services_authorization(request):
    new_leave =newleave.objects.filter(department_head_authorization="Approved", department="GOV" )
    if new_leave.exists():
        return render_to_response('GOV1_display_approve_leave.html', locals())
    else:
        return render_to_response('new_leave_for_to_be_approve_messaage.html')


def FMKD1_leave_to_authorize(request):
    new_leave =newleave.objects.filter(department_head_authorization="Approved", department="FMKD" )
    #new_leave = newleave.objects.filter(department="FMKD")
    if new_leave.exists():
        return render_to_response('FMKD1_display_approve_leave.html', locals())
    else:
        return render_to_response('new_leave_for_to_be_approve_messaage.html')

def CSD1_leave_to_authorize(request):
     new_leave =newleave.objects.filter(department_head_authorization="Approved", department="CSD")
     if new_leave.exists():
        return render_to_response('CSD1_display_approve_leave.html', locals())
     else:
        return render_to_response('new_leave_for_to_be_approve_messaage.html')


def ACSD1_leave_to_authorize(request):
    new_leave =newleave.objects.filter(department_head_authorization="Approved", department="ACSD" )
    if new_leave.exists():
        return render_to_response('ACSD1_display_approve_leave.html', locals())
    else:
        return render_to_response('new_leave_for_to_be_approve_messaage.html')


def RSHD1_leave_to_authorize(request):
    new_leave =newleave.objects.filter(department_head_authorization="Approved", department="RSHD" )
    if new_leave.exists():
        return render_to_response('RSHD1_display_approve_leave.html', locals())
    else:
        return render_to_response('new_leave_for_to_be_approve_messaage.html')

def FISD1_leave_to_authorize(request):
    new_leave =newleave.objects.filter(department_head_authorization="Approved", department="FISD" )
    if new_leave.exists():
        return render_to_response('FISD1_display_approve_leave.html', locals())
    else:
        return render_to_response('new_leave_for_to_be_approve_messaage.html')
    #-------------End coporate services authorization------------------#



#Display page to approve leave
def page_to_approve_leave(request):
    return render_to_response('Display_to_athorizeleave.html')

#Display department to approve leave by department head
def department_to_approve_leave(request):
    return render_to_response('department_approveal.html')


    #Leave Authorizer to manage leave begin
    #############################################
#Department to approved leave testing
#############################################

#Display department to approve leave by Unit head
def unit_department_to_approve_leave(request):
    return render_to_response('unitdepartment_approvial.html')

#Display department to approve leave by Directors
def unit_director_to_approve_leave(request):
    return render_to_response('unitdirector_approvial.html')

#display_foregin_exchange.html
def department_to_approve_leavetest(request):
    t = loader.get_template("approveal_processing.html")
    test=newleave.objects.filter(department="GOV",department_head_authorization="").count()
    test1=newleave.objects.filter(department="GOV",department_head_authorization="Approved").count()
    c = RequestContext(request, {'test': test,'test1': test1})
    return HttpResponse(t.render(c))

#unit director to approve leave
def department_to_approve_leavegov1(request):
    t = loader.get_template("gov1approveal_processing.html")
    test=newleave.objects.filter(department="GOV",department_head_authorization="Approved",Director_authorization="").count()
    test1=newleave.objects.filter(department="GOV",department_head_authorization="Approved",Director_authorization="Approved").count()
    c = RequestContext(request, {'test': test,'test1': test1})
    return HttpResponse(t.render(c))


def Gov111(request):
    if request.user.username=='sathy'or request.user.username=='sabiut'or request.user.username=='ptari':
        new_leave =newleave.objects.filter(department="GOV",department_head_authorization="Approved",Director_authorization="Approved")
       # if new_leave.exists():
        return render_to_response('GOV1_display_approve_leave.html', locals())
    else:
        return render_to_response('leave_authorizor_redirector.html', {'full_name': request.user.first_name })


def Gov11approved(request):
    if request.user.username=='sathy'or request.user.username=='sabiut'or request.user.username=='ptari':
        new_leave =newleave.objects.filter(department="GOV",department_head_authorization="Approved",Director_authorization="")
       # if new_leave.exists():
        return render_to_response('GOV1_display_approve_leave.html', locals())
    else:
        return render_to_response('leave_authorizor_redirector.html', {'full_name': request.user.first_name })


#display_foregin_exchange.html
def department_to_approve_leavefmd(request):
    t = loader.get_template("fmdapproveal_processing.html")
    test=newleave.objects.filter(department="FMKD",department_head_authorization="").count()
    test1=newleave.objects.filter(department="FMKD",department_head_authorization="Approved").count()
    c = RequestContext(request, {'test': test,'test1': test1})
    return HttpResponse(t.render(c))



#unit director to approve leave
def department_to_approve_leavefmd1(request):
    t = loader.get_template("fmd1approveal_processing.html")
    test=newleave.objects.filter(department="FMKD",department_head_authorization="Approved",Director_authorization="").count()
    test1=newleave.objects.filter(department="FMKD",department_head_authorization="Approved",Director_authorization="Approved").count()
    c = RequestContext(request, {'test': test,'test1': test1})
    return HttpResponse(t.render(c))


def fmd111(request):
    if request.user.username=='parubilake'or request.user.username=='sabiut'or request.user.username=='ptari'or request.user.username=='sathy':
        new_leave =newleave.objects.filter(department_head_authorization="Approved", department="FMKD",Director_authorization="Approved" )
       # if new_leave.exists():
        return render_to_response('FMKD1_display_approve_leave.html', locals())
    else:
        return render_to_response('leave_authorizor_redirector.html', {'full_name': request.user.first_name })



def fmd11approved(request):
    if request.user.username=='sathy'or request.user.username=='sabiut'or request.user.username=='ptari' or request.user.username=='parubilake':
        new_leave =newleave.objects.filter(department="FMKD",department_head_authorization="Approved",Director_authorization="")
       # if new_leave.exists():
        return render_to_response('GOV1_display_approve_leave.html', locals())
    else:
        return render_to_response('leave_authorizor_redirector.html', {'full_name': request.user.first_name })

#display_foregin_exchange.html
def department_to_approve_leavecsd(request):
    t = loader.get_template("csdapproveal_processing.html")
    test=newleave.objects.filter(department="CSD",department_head_authorization="").count()
    test1=newleave.objects.filter(department="CSD",department_head_authorization="Approved").count()
    c = RequestContext(request, {'test': test,'test1': test1})
    return HttpResponse(t.render(c))


#unit director to approve leave
def department_to_approve_leavecsd1(request):
    t = loader.get_template("csd1approveal_processing.html")
    test=newleave.objects.filter(department="CSD",department_head_authorization="Approved",Director_authorization="").count()
    test1=newleave.objects.filter(department="CSD",department_head_authorization="Approved",Director_authorization="Approved").count()
    c = RequestContext(request, {'test': test,'test1': test1})
    return HttpResponse(t.render(c))



def csd111(request):
    if request.user.username=='nshem'or request.user.username=='sabiut'or request.user.username=='ptari' or request.user.username=='sathy':
         new_leave =newleave.objects.filter( department="CSD",department_head_authorization="Approved",Director_authorization="Approved" )

         #if new_leave.exists():
         return render_to_response('CSD1_display_approve_leave.html', locals())
    else:
        return render_to_response('leave_authorizor_redirector.html', {'full_name': request.user.first_name })


def csd11approved(request):
    if request.user.username=='sathy'or request.user.username=='sabiut'or request.user.username=='ptari' or request.user.username=='nshem':
        new_leave =newleave.objects.filter(department="CSD",department_head_authorization="Approved",Director_authorization="")
       # if new_leave.exists():
        return render_to_response('GOV1_display_approve_leave.html', locals())
    else:
        return render_to_response('leave_authorizor_redirector.html', {'full_name': request.user.first_name })


#display_ACSD
def department_to_approve_leaveacsd(request):
    t = loader.get_template("acsdapproveal_processing.html")
    test=newleave.objects.filter(department="ACSD",department_head_authorization="").count()
    test1=newleave.objects.filter(department="ACSD",department_head_authorization="Approved").count()
    c = RequestContext(request, {'test': test,'test1': test1})
    return HttpResponse(t.render(c))


#unit director to approve leave
def department_to_approve_leaveacsd1(request):
    t = loader.get_template("acsd1approveal_processing.html")
    test=newleave.objects.filter(department="ACSD",department_head_authorization="Approved",Director_authorization="").count()
    test1=newleave.objects.filter(department="ACSD",department_head_authorization="Approved",Director_authorization="Approved").count()
    c = RequestContext(request, {'test': test,'test1': test1})
    return HttpResponse(t.render(c))


def acsd111(request):
    if request.user.username=='faru'or request.user.username=='sabiut'or request.user.username=='ptari' or request.user.username=='sathy':
         new_leave =newleave.objects.filter(department_head_authorization="Approved", department="ACSD",Director_authorization="Approved" )
         #if new_leave.exists():
         return render_to_response('ACSD1_display_approve_leave.html', locals())
    else:
        return render_to_response('leave_authorizor_redirector.html', {'full_name': request.user.first_name })

def acsd11approved(request):
    if request.user.username=='sathy'or request.user.username=='sabiut'or request.user.username=='ptari'or request.user.username=='faru':
        new_leave =newleave.objects.filter(department="ACSD",department_head_authorization="Approved",Director_authorization="")
       # if new_leave.exists():
        return render_to_response('GOV1_display_approve_leave.html', locals())
    else:
        return render_to_response('leave_authorizor_redirector.html', {'full_name': request.user.first_name })


#display_RSD
def department_to_approve_leavearsd(request):
    t = loader.get_template("rsddapproveal_processing.html")
    test=newleave.objects.filter(department="RSD",department_head_authorization="").count()
    test1=newleave.objects.filter(department="RSD",department_head_authorization="Approved").count()
    c = RequestContext(request, {'test': test,'test1': test1})
    return HttpResponse(t.render(c))

#unit director to approve leave
def department_to_approve_leavearsd1(request):
    t = loader.get_template("rsd1approveal_processing.html")
    test=newleave.objects.filter(department="RSD",department_head_authorization="Approved",Director_authorization="").count()
    test1=newleave.objects.filter(department="RSD",department_head_authorization="Approved",Director_authorization="Approved").count()
    c = RequestContext(request, {'test': test,'test1': test1})
    return HttpResponse(t.render(c))


def rsd111(request):
    if request.user.username=='faru'or request.user.username=='sabiut'or request.user.username=='ptari' or request.user.username=='sathy':
         new_leave =newleave.objects.filter(department_head_authorization="Approved", department="RSD",Director_authorization="Approved" )
         #if new_leave.exists():
         return render_to_response('GOV1_display_approve_leave.html', locals())
    else:
        return render_to_response('leave_authorizor_redirector.html', {'full_name': request.user.first_name })

def rsd11approved(request):
    if request.user.username=='gsiri'or request.user.username=='sabiut'or request.user.username=='ptari' or request.user.username=='sathy':
         new_leave =newleave.objects.filter(department_head_authorization="Approved", department="RSD",Director_authorization="" )
         #if new_leave.exists():
         return render_to_response('GOV1_display_approve_leave.html', locals())
    else:
        return render_to_response('leave_authorizor_redirector.html', {'full_name': request.user.first_name })



#display_FISD
def department_to_approve_leaveafsd(request):
    t = loader.get_template("fisdapproveal_processing.html")
    test=newleave.objects.filter(department="FISD",department_head_authorization="").count()
    test1=newleave.objects.filter(department="FISD",department_head_authorization="Approved").count()
    c = RequestContext(request, {'test': test,'test1': test1})
    return HttpResponse(t.render(c))


#unit director to approve leave
def department_to_approve_leaveafisd1(request):
    t = loader.get_template("fisd1approveal_processing.html")
    test=newleave.objects.filter(department="FISD",department_head_authorization="Approved",Director_authorization="").count()
    test1=newleave.objects.filter(department="FISD",department_head_authorization="Approved",Director_authorization="Approved").count()
    c = RequestContext(request, {'test': test,'test1': test1})
    return HttpResponse(t.render(c))


def fisd111(request):
    if request.user.username=='nvari'or request.user.username=='sabiut'or request.user.username=='ptari' or request.user.username=='sathy':
         new_leave =newleave.objects.filter(department_head_authorization="Approved", department="FISD",Director_authorization="Approved" )
         #if new_leave.exists():
         return render_to_response('GOV1_display_approve_leave.html', locals())
    else:
        return render_to_response('leave_authorizor_redirector.html', {'full_name': request.user.first_name })

def fisd11approved(request):
    if request.user.username=='nvari'or request.user.username=='sabiut'or request.user.username=='ptari' or request.user.username=='sathy':
         new_leave =newleave.objects.filter(department_head_authorization="Approved", department="FISD",Director_authorization="" )
         #if new_leave.exists():
         return render_to_response('GOV1_display_approve_leave.html', locals())
    else:
        return render_to_response('leave_authorizor_redirector.html', {'full_name': request.user.first_name })

#Leave authorizer to manage leave ends


    #Display Leave
def leave_view(request):
     #return render_to_response('display.html')
    leaves=leave.objects.all()
    return render_to_response('leave.html', locals())

def govoffice(request):
    govstaff=newleave.objects.filter(department="GOV",department_head_authorization="Approved",Director_authorization="Approved",process_bal="")
    return render(request,'gov_office.html', locals())


def fmdkoffice(request):
    fmkdtaff=newleave.objects.filter(department="FMKD",department_head_authorization="Approved",Director_authorization="Approved",process_bal="")
    return render(request,'fmdk_office.html', locals())


def csdoffice(request):
    csdtaff=newleave.objects.filter(department="CSD",department_head_authorization="Approved",Director_authorization="Approved",process_bal="")
    return render(request,'csd_office.html', locals())

def acsdoffice(request):
    acsdstaff=newleave.objects.filter(department="ACSD",department_head_authorization="Approved",Director_authorization="Approved",process_bal="")
    return render(request,'acsd_office.html', locals())

def rshdoffice(request):
    rsdstaff=newleave.objects.filter(department="RSD",department_head_authorization="Approved",Director_authorization="Approved",process_bal="")
    return render(request,'rshd_office.html', locals())

def fisdoffice(request):
    fisdstaff=newleave.objects.filter(department="FISD",department_head_authorization="Approved",Director_authorization="Approved",process_bal="")
    return render(request,'fisd_office.html', locals())

#FUNCTION TO UPDATE TABLE
def update_form(request, id):
    if request.method == 'POST':
        a=newleave.objects.get(id=id)
        form =leave_application(request.POST, instance=a)
        if form.is_valid():
           form.save()
        return render_to_response('successful.html')
    else:
        a=newleave.objects.get(id=id)
        form = leave_application(instance=a)
    return render_to_response('update_form.html', {'form': form}, context_instance=RequestContext(request))


#FUNCTION TO UPDATE TABLE
def update_form(request, id):
    if request.method == 'POST':
        a=newleave.objects.get(id=id)
        form =leave_application(request.POST, instance=a)
        if form.is_valid():
           form.save()
        return render_to_response('successful.html')
    else:
        a=newleave.objects.get(id=id)
        form = leave_application(instance=a)
    return render_to_response('update_form.html', {'form': form}, context_instance=RequestContext(request))



#Function to Authorize Leave
def authorized_Leave(request, id):
    if request.method == 'POST':
        a=newleave.objects.get(id=id)
        form = authoriseleave(request.POST, instance=a)
        if form.is_valid():
           form.save()
        to_emails =[a.username.email]
        if a.department_head_authorization=="Approved":
           #to_emails =[a.username.email]
           send_mail("Leave Application Approved by"+" "+ a.authorized_by, "Your Leave Application have been {}".format(a.department_head_authorization)+" "+"by your Manager {}".format(a.authorized_by) +" "+"and is now being forward to the Diretor for second authorization.\nYou will be inform by email once Authorized by the Director.",
           "RBV eLeave <eLeavesystem@rbv.gov.vu>", to_emails)
           to_emails =[a.username.email]
        elif a.department_head_authorization=="Rejected":
             send_mail("Leave Application Rejected by"+" "+ a.authorized_by , "Your Leave Application have been {}".format(a.department_head_authorization)+" "+"by your Manager {}".format(a.authorized_by)+". "+"Contact your Manager for more info",
           "RBV eLeave <eLeavesystem@rbv.gov.vu>", to_emails)
        return render_to_response('authorized_message.html')
    else:
        a=newleave.objects.get(id=id)
        form =  authoriseleave(instance=a)
    return render_to_response('approve_leave.html', {'form': form}, context_instance=RequestContext(request))


def coporateservices_authorized_Leave(request, id):
    if request.method == 'POST':
        a=newleave.objects.get(id=id)
        form = coporateservices_authoriseleave(request.POST, instance=a)
        if form.is_valid():
            form.save()
            to_emails=[a.username.email]
            if a.Director_authorization=="Approved":
                send_mail("Leave Application Approved by"+" "+a.Authorization_by, "Your Leave Application have been {}".format(a.Director_authorization)+" "+" by the Director {}".format(a.Authorization_by),
                "RBV eLeave <eLeavesystem@rbv.gov.vu>", to_emails)
            elif a.Director_authorization=="Rejected":
                send_mail("Leave Application Rejected by"+" "+ a.Authorization_by, "Your Leave Application have been {}".format(a.Director_authorization)+" "+"by your Director {}".format(a.Authorization_by)+". "+"Contact your Manager for more info",
            "RBV eLeave <eLeavesystem@rbv.gov.vu>", to_emails)
        return render_to_response('authorized_message.html')
    else:
        a=newleave.objects.get(id=id)
        form =  coporateservices_authoriseleave(instance=a)
        return render_to_response('coporate_services_leave_approvial.html', {'form': form}, context_instance=RequestContext(request))


#send email to Authorizer
def email_authorizer(request):
    email_obj = newleave.objects.order_by('-pk')[0]
    if email_obj.department == 'GOV':
        to_emails = [u.email for u in User.objects.filter(username__in=['klunabek', 'sabiut','ptari','twarsal','sathy'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
        "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
        to_emails = [u.email for u in User.objects.filter(username__in=['klunabek', 'sabiut'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to calculate leave current balance.",
        "RBV eLeave Calculator <eLeavesystem@rbv.gov.vu>", [to_emails])
        return render_to_response('thankyou.html')


    elif  email_obj.first_name == 'Simeon' or email_obj.first_name == 'simeon':
        to_emails = [u.email for u in User.objects.filter(username__in=['ptari'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
        "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
        to_emails = [u.email for u in User.objects.filter(username__in=[ 'klunabek','sabiut'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to calculate leave current balance.",
        "RBV eLeave Calculator <eLeavesystem@rbv.gov.vu>", [to_emails])
        return render_to_response('thankyou.html')

    elif  email_obj.first_name == 'Peter' or email_obj.first_name == 'peter':
        to_emails = [u.email for u in User.objects.filter(username__in=['sathy'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
        "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
        to_emails = [u.email for u in User.objects.filter(username__in=[ 'klunabek','sabiut'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to calculate leave current balance.",
        "RBV eLeave Calculator <eLeavesystem@rbv.gov.vu>", [to_emails])
        return render_to_response('thankyou.html')

    elif  email_obj.first_name == 'Michael' or email_obj.first_name == 'michael':
        to_emails = [u.email for u in User.objects.filter(username__in=['ptari','sathy'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
        "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
        to_emails = [u.email for u in User.objects.filter(username__in=[ 'klunabek','sabiut'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to calculate leave current balance.",
        "RBV eLeave Calculator <eLeavesystem@rbv.gov.vu>", [to_emails])
        return render_to_response('thankyou.html')

    elif  email_obj.first_name == 'Branan' or email_obj.first_name == 'branan':
        to_emails = [u.email for u in User.objects.filter(username__in=['ptari','sathy'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
        "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
        to_emails = [u.email for u in User.objects.filter(username__in=[ 'klunabek','sabiut'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to calculate leave current balance.",
        "RBV eLeave Calculator <eLeavesystem@rbv.gov.vu>", [to_emails])
        return render_to_response('thankyou.html')

    elif  email_obj.first_name == 'Linnes' or email_obj.first_name == 'linnes':
        to_emails = [u.email for u in User.objects.filter(username__in=['ptari','sathy'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
        "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
        to_emails = [u.email for u in User.objects.filter(username__in=[ 'klunabek','sabiut'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to calculate leave current balance.",
        "RBV eLeave Calculator <eLeavesystem@rbv.gov.vu>", [to_emails])
        return render_to_response('thankyou.html')

    elif email_obj.department=='CSD':
            to_emails = [u.email for u in User.objects.filter(username__in=['klunabek', 'sabiut','nshem','aterry','ljonas'])]
            send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
            "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
            return render_to_response('thankyou.html')

    elif  email_obj.first_name == 'Nelson' or email_obj.first_name == 'nelson':
        to_emails = [u.email for u in User.objects.filter(username__in=['ptari','sathy'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
        "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
        to_emails = [u.email for u in User.objects.filter(username__in=[ 'klunabek','sabiut'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to calculate leave current balance.",
        "RBV eLeave Calculator <eLeavesystem@rbv.gov.vu>", [to_emails])
        return render_to_response('thankyou.html')

    elif  email_obj.first_name == 'Jessica' or email_obj.first_name == 'jessica':
        to_emails = [u.email for u in User.objects.filter(username__in=['nshem'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
        "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
        to_emails = [u.email for u in User.objects.filter(username__in=[ 'klunabek','sabiut'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to calculate leave current balance.",
        "RBV eLeave Calculator <eLeavesystem@rbv.gov.vu>", [to_emails])
        return render_to_response('thankyou.html')

    elif  email_obj.first_name == 'Lonneth' or email_obj.first_name == 'lonneth':
        to_emails = [u.email for u in User.objects.filter(username__in=['nshem'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
        "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
        to_emails = [u.email for u in User.objects.filter(username__in=[ 'klunabek','sabiut'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to calculate leave current balance.",
        "RBV eLeave Calculator <eLeavesystem@rbv.gov.vu>", [to_emails])
        return render_to_response('thankyou.html')

    elif  email_obj.first_name == 'Alick' or email_obj.first_name == 'alick':
        to_emails = [u.email for u in User.objects.filter(username__in=['nshem'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
        "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
        to_emails = [u.email for u in User.objects.filter(username__in=[ 'klunabek','sabiut'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to calculate leave current balance.",
        "RBV eLeave Calculator <eLeavesystem@rbv.gov.vu>", [to_emails])
        return render_to_response('thankyou.html')


    elif email_obj.department=='FMKD':
            to_emails = [u.email for u in User.objects.filter(username__in=['klunabek', 'sabiut','parubilake','lstephens'])]
            send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
            "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
            return render_to_response('thankyou.html')

    elif  email_obj.first_name == 'Philip' or email_obj.first_name == 'philip':
        to_emails = [u.email for u in User.objects.filter(username__in=['ptari','sathy'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
        "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
        to_emails = [u.email for u in User.objects.filter(username__in=[ 'klunabek','sabiut'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to calculate leave current balance.",
        "RBV eLeave Calculator <eLeavesystem@rbv.gov.vu>", [to_emails])
        return render_to_response('thankyou.html')

    elif  email_obj.first_name == 'Victoria' or email_obj.first_name == 'victoria':
        to_emails = [u.email for u in User.objects.filter(username__in=['parubilake'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
        "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
        to_emails = [u.email for u in User.objects.filter(username__in=[ 'klunabek','sabiut'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to calculate leave current balance.",
        "RBV eLeave Calculator <eLeavesystem@rbv.gov.vu>", [to_emails])
        return render_to_response('thankyou.html')




    elif email_obj.department=='ACSD':
            to_emails = [u.email for u in User.objects.filter(username__in=['klunabek', 'sabiut','kseri','faru','halilee','smarum','FBeru'])]
            send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
            "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
            return render_to_response('thankyou.html')

    elif  email_obj.first_name == 'Florinda' or email_obj.first_name == 'florinda':
        to_emails = [u.email for u in User.objects.filter(username__in=['ptari','sathy'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
        "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
        to_emails = [u.email for u in User.objects.filter(username__in=[ 'klunabek','sabiut'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to calculate leave current balance.",
        "RBV eLeave Calculator <eLeavesystem@rbv.gov.vu>", [to_emails])
        return render_to_response('thankyou.html')

    elif  email_obj.first_name == 'Carolyn' or email_obj.first_name == 'carolyn':
        to_emails = [u.email for u in User.objects.filter(username__in=['faru'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
        "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
        to_emails = [u.email for u in User.objects.filter(username__in=[ 'klunabek','sabiut'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to calculate leave current balance.",
        "RBV eLeave Calculator <eLeavesystem@rbv.gov.vu>", [to_emails])
        return render_to_response('thankyou.html')

    elif  email_obj.first_name == 'Kensen' or email_obj.first_name == 'kensen':
        to_emails = [u.email for u in User.objects.filter(username__in=['faru'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
        "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
        to_emails = [u.email for u in User.objects.filter(username__in=[ 'klunabek','sabiut'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to calculate leave current balance.",
        "RBV eLeave Calculator <eLeavesystem@rbv.gov.vu>", [to_emails])
        return render_to_response('thankyou.html')

    elif  email_obj.first_name == 'Sereana' or email_obj.first_name == 'sereana':
        to_emails = [u.email for u in User.objects.filter(username__in=['faru'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
        "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
        to_emails = [u.email for u in User.objects.filter(username__in=[ 'klunabek','sabiut'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to calculate leave current balance.",
        "RBV eLeave Calculator <eLeavesystem@rbv.gov.vu>", [to_emails])
        return render_to_response('thankyou.html')


    elif email_obj.department=='RSD':
            to_emails = [u.email for u in User.objects.filter(username__in=['klunabek', 'sabiut','gsiri','cala','akaltongga','lragonmal'])]
            send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
            "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
            return render_to_response('thankyou.html')

    elif  email_obj.first_name == 'Gloria' or email_obj.first_name == 'gloria':
        to_emails = [u.email for u in User.objects.filter(username__in=['ptari','sathy'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
        "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
        to_emails = [u.email for u in User.objects.filter(username__in=[ 'klunabek','sabiut'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to calculate leave current balance.",
        "RBV eLeave Calculator <eLeavesystem@rbv.gov.vu>", [to_emails])
        return render_to_response('thankyou.html')

    elif  email_obj.first_name == 'Linda' or email_obj.first_name == 'linda':
        to_emails = [u.email for u in User.objects.filter(username__in=['gsiri'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
        "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
        to_emails = [u.email for u in User.objects.filter(username__in=[ 'klunabek','sabiut'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to calculate leave current balance.",
        "RBV eLeave Calculator <eLeavesystem@rbv.gov.vu>", [to_emails])
        return render_to_response('thankyou.html')

    elif  email_obj.first_name == 'Alumeci' or email_obj.first_name == 'alumeci':
        to_emails = [u.email for u in User.objects.filter(username__in=['gsiri'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
        "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
        to_emails = [u.email for u in User.objects.filter(username__in=[ 'klunabek','sabiut'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to calculate leave current balance.",
        "RBV eLeave Calculator <eLeavesystem@rbv.gov.vu>", [to_emails])
        return render_to_response('thankyou.html')

    elif  email_obj.first_name == 'Pita' or email_obj.first_name == 'pita':
        to_emails = [u.email for u in User.objects.filter(username__in=['gsiri'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
        "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
        to_emails = [u.email for u in User.objects.filter(username__in=[ 'klunabek','sabiut'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to calculate leave current balance.",
        "RBV eLeave Calculator <eLeavesystem@rbv.gov.vu>", [to_emails])
        return render_to_response('thankyou.html')

    elif  email_obj.last_name == 'Ala' or email_obj.last_name == 'ala':
        to_emails = [u.email for u in User.objects.filter(username__in=['gsiri'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
        "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
        to_emails = [u.email for u in User.objects.filter(username__in=[ 'klunabek','sabiut'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to calculate leave current balance.",
        "RBV eLeave Calculator <eLeavesystem@rbv.gov.vu>", [to_emails])
        return render_to_response('thankyou.html')

    elif  email_obj.first_name == 'Lynette' or email_obj.first_name == 'lynette':
        to_emails = [u.email for u in User.objects.filter(username__in=['gsiri'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
        "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
        to_emails = [u.email for u in User.objects.filter(username__in=[ 'klunabek','sabiut'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to calculate leave current balance.",
        "RBV eLeave Calculator <eLeavesystem@rbv.gov.vu>", [to_emails])
        return render_to_response('thankyou.html')


    elif email_obj.department=='FISD':
            to_emails = [u.email for u in User.objects.filter(username__in=['klunabek', 'sabiut','nvari','mmera','mabbil'])]
            send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
            "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
            return render_to_response('thankyou.html')

    elif  email_obj.first_name == 'Noel' or email_obj.first_name == 'noel':
        to_emails = [u.email for u in User.objects.filter(username__in=['ptari','sathy'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
        "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
        to_emails = [u.email for u in User.objects.filter(username__in=[ 'klunabek','sabiut'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to calculate leave current balance.",
        "RBV eLeave Calculator <eLeavesystem@rbv.gov.vu>", [to_emails])
        return render_to_response('thankyou.html')

    elif  email_obj.last_name == 'Mabon' or email_obj.last_name == 'mabon':
        to_emails = [u.email for u in User.objects.filter(username__in=['nvari'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
        "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
        to_emails = [u.email for u in User.objects.filter(username__in=[ 'klunabek','sabiut'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to calculate leave current balance.",
        "RBV eLeave Calculator <eLeavesystem@rbv.gov.vu>", [to_emails])
        return render_to_response('thankyou.html')

    elif  email_obj.first_name == 'Mark' or email_obj.first_name == 'mark':
        to_emails = [u.email for u in User.objects.filter(username__in=['nvari'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
        "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
        to_emails = [u.email for u in User.objects.filter(username__in=[ 'klunabek','sabiut'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to calculate leave current balance.",
        "RBV eLeave Calculator <eLeavesystem@rbv.gov.vu>", [to_emails])
        return render_to_response('thankyou.html')

    elif  email_obj.first_name == 'Marinette' or email_obj.first_name == 'marinette':
        to_emails = [u.email for u in User.objects.filter(username__in=['nvari'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to Authorize the leave.",
        "RBV eLeave <eLeavesystem@rbv.gov.vu>", [to_emails])
        to_emails = [u.email for u in User.objects.filter(username__in=[ 'klunabek','sabiut'])]
        send_mail(email_obj.first_name+" " + email_obj.last_name+" "+"RBV Leave Application", email_obj.first_name+" " + email_obj.last_name+ " "+"have apply for a leave. Please login to http://eleave:8000/eLeave to calculate leave current balance.",
        "RBV eLeave Calculator <eLeavesystem@rbv.gov.vu>", [to_emails])
        return render_to_response('thankyou.html')


  #Leave Calculator
def leave_calculator(request, id):
    if request.method == 'POST':
        a=newleave.objects.get(id=id)
        form = leavecalculator(request.POST, instance=a)
        if form.is_valid():
            leavetotal=a.leave_outstanding_balance
            leaveentitlement=a.leave_entitlement
            numberofdays =a.total_working_days
            holidays=a.holiday
            weekends=a.weekend
            currentbalance= leavetotal+leaveentitlement-numberofdays+holidays+weekends
            a.leave_current_balance= currentbalance
            form.save()
            return render_to_response('Leave_calculate_message.html')
    else:
        a=newleave.objects.get(id=id)
        form =  leavecalculator(instance=a)
        return render_to_response('calculateleave.html', {'form': form}, context_instance=RequestContext(request))


#Accessing HR Office
def hroffice(request):
    if request.user.username=='klunabek'or request.user.username=='sabiut'or request.user.username=='admin' or request.user.username=='amolisa':
        return render_to_response('hr_office.html', {'full_name': request.user.first_name}, context_instance=RequestContext(request))
    else:
        return render_to_response('hr_redirect.html', {'full_name': request.user.first_name })


#Leave authorizor Redirector
def Gov1(request):
    if request.user.username=='sathy' or request.user.username=='ptari' or request.user.username=='twarsal'or request.user.username=='klunabek':
        new_leave=newleave.objects.filter(department="GOV",department_head_authorization="")
        return render_to_response('GOV_display_approve_leave.html', locals())
    else:
        return render_to_response('leave_authorizor_redirector.html', {'full_name': request.user.first_name })

def fmkd1(request):
    if request.user.username=='ptari'or request.user.username=='sathy' or request.user.username=='parubilake' or request.user.username=='lstephens':
        new_leave=newleave.objects.filter(department="FMKD",department_head_authorization="")
        return render_to_response('FMKD_display_approve_leave.html', locals())
    else:
        return render_to_response('leave_authorizor_redirector.html', {'full_name': request.user.first_name })

def csd1(request):
    if request.user.username=='ptari'or request.user.username=='sathy' or request.user.username=='nshem' or request.user.username=='aterry' or request.user.username=='ljonas':
        new_leave=newleave.objects.filter(department="CSD",department_head_authorization="")
        return render_to_response('CSD_display_approve_leave.html', locals())
    else:
        return render_to_response('leave_authorizor_redirector.html', {'full_name': request.user.first_name })


def acsd1(request):
    if request.user.username=='faru'or request.user.username=='smarum'or request.user.username=='sathy'or request.user.username=='ptari'or request.user.username=='kseri' or request.user.username=='halilee':
        new_leave=newleave.objects.filter(department="ACSD",department_head_authorization="")
        return render_to_response('ACSD_display_approve_leave.html', locals())
    else:
        return render_to_response('leave_authorizor_redirector.html', {'full_name': request.user.first_name })


def rshd1(request):
    if request.user.username=='akaltongga'or request.user.username=='sathy' or request.user.username=='gsiri' or request.user.username=='ptari'or request.user.username=='cala'or request.user.username=='lragonmal':
        new_leave=newleave.objects.filter(department="RSD",department_head_authorization="")
        return render_to_response('RSHD_display_approve_leave.html', locals())
    else:
        return render_to_response('leave_authorizor_redirector.html', {'full_name': request.user.first_name })


def fisd1(request):
    if request.user.username=='sabiut' or request.user.username=='sathy'or request.user.username=='ptari' or request.user.username=='nvari' or request.user.username=='mmera'or request.user.username=='mabbil':
        new_leave=newleave.objects.filter(department="FISD",department_head_authorization="")
        return render_to_response('FISD_display_approve_leave.html', locals())
    else:
        return render_to_response('leave_authorizor_redirector.html', {'full_name': request.user.first_name })



#Leave Cooperate services authorizor Redirector
def Gov11(request):
    if request.user.username=='sathy'or request.user.username=='sabiut'or request.user.username=='ptari'or request.user.username=='twarsal'or request.user.username=='klunabek':
        new_leave =newleave.objects.filter(department_head_authorization="Approved", department="GOV" )
       # if new_leave.exists():
        return render_to_response('GOV1_display_approve_leave.html', locals())
    else:
        return render_to_response('leave_authorizor_redirector.html', {'full_name': request.user.first_name })

def fmkd11(request):
    if request.user.username=='parubilake'or request.user.username=='sabiut'or request.user.username=='ptari'or request.user.username=='sathy':
        new_leave =newleave.objects.filter(department_head_authorization="Approved", department="FMKD" )
       # if new_leave.exists():
        return render_to_response('FMKD1_display_approve_leave.html', locals())
    else:
        return render_to_response('leave_authorizor_redirector.html', {'full_name': request.user.first_name })

def csd11(request):
    if request.user.username=='nshem'or request.user.username=='sabiut'or request.user.username=='ptari' or request.user.username=='sathy':
         new_leave =newleave.objects.filter(department_head_authorization="Approved", department="CSD")
         #if new_leave.exists():
         return render_to_response('CSD1_display_approve_leave.html', locals())
    else:
        return render_to_response('leave_authorizor_redirector.html', {'full_name': request.user.first_name })

def acsd11(request):
    if request.user.username=='faru'or request.user.username=='sabiut'or request.user.username=='ptari' or request.user.username=='sathy':
         new_leave =newleave.objects.filter(department_head_authorization="Approved", department="ACSD" )
         #if new_leave.exists():
         return render_to_response('ACSD1_display_approve_leave.html', locals())
    else:
        return render_to_response('leave_authorizor_redirector.html', {'full_name': request.user.first_name })

def rshd11(request):
    if request.user.username=='gsiri'or request.user.username=='sabiut'or request.user.username=='ptari' or request.user.username=='sathy'or request.user.username=='cala':
         new_leave =newleave.objects.filter(department_head_authorization="Approved", department="RSD" )
         #if new_leave.exists():
         return render_to_response('RSHD1_display_approve_leave.html', locals())
    else:
        return render_to_response('leave_authorizor_redirector.html', {'full_name': request.user.first_name })


def fisd11(request):
    if request.user.username=='nvari'or request.user.username=='sabiut'or request.user.username=='ptari' or request.user.username=='sathy':
        new_leave =newleave.objects.filter(department_head_authorization="Approved", department="FISD" )
        #if new_leave.exists():
        return render_to_response('FISD1_display_approve_leave.html', locals())
    else:
        return render_to_response('leave_authorizor_redirector.html', {'full_name': request.user.first_name })





#FUNCTION TO UPDATE Leave Form TABLE
def update_Leaveform(request, id):
    if request.method == 'POST':
        a=newleave.objects.get(id=id)
        form =leave_application(request.POST, instance=a)
        if form.is_valid():
           form.save()
        return render_to_response('leave_successful.html')
    else:
        a=newleave.objects.get(id=id)
        form = leave_application(instance=a)
    return render_to_response('update_form.html', {'form': form}, context_instance=RequestContext(request))


#view Leave applicant
def view_leave_info(request):
    leave_in=newleave.objects.all()
    return render_to_response('all_leave.html',locals())

#Testing staff info
#def leave_info(request):
    #staffinfo=leave.objects.filter()
    #return render_to_response('display_staffinfo.html', locals())

#export file to CSV
#export file to CSV
def staff_info_csv(request):
    csv_export=new_staff.objects.values('first_name','last_name','gender','date_of_birth','marital_status','nationality','home_island','dependants','relationship_to_you','postal_Address','employee_Date','position','department','vnpf_no','bank_name','account_number')
    return djqscsv.render_to_csv_response(csv_export)


def leave_info_csv(request):
    csv_export=newleave.objects.values('first_name','last_name','department','position','leave_type','specify_details','start_date','end_date',
    'total_working_days','department_head_authorization','authorized_by','remarks','authorization_date','Director_authorization',
    'Authorization_by','Director_remarks','Authoriztaion_date','month','year','leave_entitlement','holiday','weekend','leave_outstanding_balance','leave_current_balance')
    return djqscsv.render_to_csv_response(csv_export)

#write to database
def write_todatabase(request):
    return render(request,'write_to_database.html')


def leaveapp(request):
    t = loader.get_template("allleave.html")
    test=newleave.objects.all().count()
    gov=newleave.objects.filter(department="GOV",department_head_authorization="Approved",Director_authorization="Approved",process_bal="").count()
    fisd=newleave.objects.filter(department="FISD",department_head_authorization="Approved",Director_authorization="Approved",process_bal="").count()
    rsd=newleave.objects.filter(department="RSD",department_head_authorization="Approved",Director_authorization="Approved",process_bal="").count()
    csd=newleave.objects.filter(department="CSD",department_head_authorization="Approved",Director_authorization="Approved",process_bal="").count()
    acsd=newleave.objects.filter(department="ACSD",department_head_authorization="Approved",Director_authorization="Approved",process_bal="").count()
    fmd=newleave.objects.filter(department="FMKD",department_head_authorization="Approved",Director_authorization="Approved",process_bal="").count()
    process=newleave.objects.filter(department="GOV",department_head_authorization="Approved",Director_authorization="Approved",process_bal="Processed").count()
    process_FISD=newleave.objects.filter(department="FISD",department_head_authorization="Approved",Director_authorization="Approved",process_bal="Processed").count()
    process_RSD=newleave.objects.filter(department="RSD",department_head_authorization="Approved",Director_authorization="Approved",process_bal="Processed").count()
    process_CSD=newleave.objects.filter(department="CSD",department_head_authorization="Approved",Director_authorization="Approved",process_bal="Processed").count()
    process_ACSD=newleave.objects.filter(department="ACSD",department_head_authorization="Approved",Director_authorization="Approved",process_bal="Processed").count()
    process_FMD=newleave.objects.filter(department="FMD",department_head_authorization="Approved",Director_authorization="Approved",process_bal="Processed").count()
    #reject=newleave.objects.filter(Director_authorization="Rejected").count()
    reject_all=newleave.objects.filter(Director_authorization="Rejected").count()
    c = RequestContext(request, {'test': test,'gov': gov,'fisd': fisd,'rsd': rsd,'csd': csd,'acsd': acsd,'process':process,'process_RSD':process_RSD,'process_CSD':process_CSD,'process_ACSD':process_ACSD,'process_FMD':process_FMD,'process_FISD':process_FISD,'reject_all':reject_all,'fmd':fmd})
    return HttpResponse(t.render(c))


#FUNCTION TO process leave balance
def process_Leaveform(request, id):
    if request.method == 'POST':
        a=newleave.objects.get(id=id)
        form = processbalanceform(request.POST, instance=a)
        if form.is_valid():
           form.save()
        return render_to_response('leave_successful.html')
    else:
        a=newleave.objects.get(id=id)
        form = processbalanceform(instance=a)
    return render_to_response('processed_balance.html', {'form': form}, context_instance=RequestContext(request))

#def display_processbal(request):
    #leave_bal=newleave.objects.filter(department="GOV",process_bal="processed")
    #return render_to_response('displayprocessbal.html',locals())




#process department balance start
def display_processbal(request):
    leave_in=newleave.objects.filter(department="GOV",process_bal="Processed")
    return render_to_response('displayprocessbal.html',locals())


def display_processfisd(request):
    leave_in=newleave.objects.filter(department="FISD",process_bal="Processed")
    return render_to_response('displayprocessbal.html',locals())

def display_processrsd(request):
    leave_in=newleave.objects.filter(department="RSD",process_bal="Processed")
    return render_to_response('displayprocessbal.html',locals())

def display_processcsd(request):
    leave_in=newleave.objects.filter(department="CSD",process_bal="Processed")
    return render_to_response('displayprocessbal.html',locals())

def display_processacsd(request):
    leave_in=newleave.objects.filter(department="ACSD",process_bal="Processed")
    return render_to_response('displayprocessbal.html',locals())

def display_processfmd(request):
    leave_in=newleave.objects.filter(department="FMD",process_bal="Processed")
    return render_to_response('displayprocessbal.html',locals())

def rejected_leaves(request):
    reject=newleave.objects.filter(Director_authorization="Rejected")
    return render_to_response('displayrejectedleave.html',locals())
#process department balance start end
