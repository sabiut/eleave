from django.conf.urls import patterns, include, url
from django.contrib import admin
from eLeave import views

#administrator headers
admin.site.site_header="RBV eLeave System Administrator"
admin.site.site_title="RBV eLeave Administration"
admin.site.index_title="RBV eLeave Administration"


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'',include('leavebalance.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^eLeave/', include('eLeave.urls')),
     #url(r'^edit_staff/', include('eLeave.urls')),
    # url(r'^create/', include('eLeave.urls')),


    #user auth urls
    url(r'^eLeave/$', 'eLeave.views.index'),
     url(r'^eLeave/loggedin/$', 'eLeave.views.loggedin'),
     url(r'^eLeave/auth/$', 'eLeave.views.auth_view'),
     url(r'^eLeave/invalid/$', 'eLeave.views.invalid'),
     url(r'^eLeave/logout/$', 'eLeave.views.logout'),

    #Accessing HR Office
     url(r'^hroffice/$', 'eLeave.views.hroffice'),

     #Authorize leave redirect
    url(r'^Gov1/$','eLeave.views.Gov1'),
    url(r'^fmkd1/$','eLeave.views.fmkd1'),
    url(r'^csd1/$','eLeave.views.csd1'),
    url(r'^acsd1/$','eLeave.views.acsd1'),
    url(r'^rshd1/$','eLeave.views.rshd1'),
    url(r'^fisd1/$','eLeave.views.fisd1'),

     #Coporate services Authorize leave redirect
     url(r'^Gov11/$','eLeave.views.Gov11'),
     url(r'^fmkd11/$','eLeave.views.fmkd11'),
      url(r'^csd11/$','eLeave.views.csd11'),
    url(r'^acsd11/$','eLeave.views.acsd11'),
    url(r'^rshd11/$','eLeave.views.rshd11'),
    url(r'^fisd11/$','eLeave.views.fisd11'),

    #Leave Form
    url(r'^leaves/$', 'eLeave.views.leaves'),
    url(r'^edit_staff/$', 'eLeave.views.edit_staff'),
    url(r'^newstaff/$', 'eLeave.views.newstaff'),
    url(r'^leaveapplication/$', 'eLeave.views.leaveapplication'),
    url(r'^leave_application2/$', 'eLeave.views.leave_application2'),


    #successfuly message
   # url(r'^successful/$', 'eLeave.views.edit_staff'),

    #display table
    url(r'^display_view/$', 'eLeave.views.display_view'),
    url(r'^govoffice/$', 'eLeave.views.govoffice'),
    url(r'^fmdkoffice/$', 'eLeave.views.fmdkoffice'),
    url(r'^csdoffice/$', 'eLeave.views.csdoffice'),
    url(r'^acsdoffice/$', 'eLeave.views.acsdoffice'),
    url(r'^rshdoffice/$', 'eLeave.views.rshdoffice'),
    url(r'^fisdoffice/$', 'eLeave.views.fisdoffice'),
    url(r'^leave_info/$', 'eLeave.views.leave_info'),
    url(r'^dispay_staff/$', 'eLeave.views.dispay_staff'),

    # Leave to authorize by department head
    url(r'^leave_to_authorize/$', 'eLeave.views.leave_to_authorize'),
    url(r'^FMKD_leave_to_authorize/$', 'eLeave.views.FMKD_leave_to_authorize'),
    url(r'^CSD_leave_to_authorize/$', 'eLeave.views.CSD_leave_to_authorize'),
    url(r'^ACSD_leave_to_authorize/$', 'eLeave.views.ACSD_leave_to_authorize'),
    url(r'^RSHD_leave_to_authorize/$', 'eLeave.views.RSHD_leave_to_authorize'),
    url(r'^FISD_leave_to_authorize/$', 'eLeave.views.FISD_leave_to_authorize'),

    # Leave to authorize by coporate services
   url(r'^coporateservices_authorization/$', 'eLeave.views.coporateservices_authorization'),
   url(r'^coporate_services_authorization/$', 'eLeave.views.coporate_services_authorization'),
   url(r'^FMKD1_leave_to_authorize/$', 'eLeave.views.FMKD1_leave_to_authorize'),
   url(r'^CSD1_leave_to_authorize/$', 'eLeave.views.CSD1_leave_to_authorize'),
   url(r'^ACSD1_leave_to_authorize/$', 'eLeave.views.ACSD1_leave_to_authorize'),
   url(r'^RSHD1_leave_to_authorize/$', 'eLeave.views.RSHD1_leave_to_authorize'),
   url(r'^FISD1_leave_to_authorize/$', 'eLeave.views.FISD1_leave_to_authorize'),






    #authorize leave display
    url(r'^page_to_approve_leave/$', 'eLeave.views.page_to_approve_leave'),
    url(r'^department_to_approve_leave/$', 'eLeave.views.department_to_approve_leave'),
    url(r'^coporateservices_authorized_Leave/(?P<id>\d+)/$', 'eLeave.views.coporateservices_authorized_Leave'),



    #display view test
     url(r'^leave_view/$', 'eLeave.views.leave_view'),

    #update Forms
    #url(r'^update_form/$', 'eLeave.views.update_form'),
    url(r'^update_form/(?P<id>\d+)/$', 'eLeave.views.update_form'),
    url(r'^authorized_Leave/(?P<id>\d+)/$', 'eLeave.views.authorized_Leave'),


    #leave update form
     #update leaveform
    url(r'^update_Leaveform/(?P<id>\d+)/$', 'eLeave.views.update_Leaveform'),
    url(r'^view_leave_info/$','eLeave.views.view_leave_info'),


    #email test
       url(r'^emailapp/sending_email/$','emailapp.views.sending_email'),
       url(r'^email_authorizer/$','eLeave.views.email_authorizer'),

    #calculate email

    url(r'^leave_calculator/(?P<id>\d+)/$','eLeave.views.leave_calculator'),


   # adding staff info
   url(r'^training_edu/$','eLeave.views.training_edu'),
   url(r'^institution_name/$','eLeave.views.institution_name'),
   url(r'^dispay_staff_training/$','eLeave.views.dispay_staff_training'),
   url(r'^dispay_staff_employment/$','eLeave.views.dispay_staff_employment'),

   # Display RBV Staff Training
   url(r'^dispay_rbv_training/$','eLeave.views.dispay_rbv_training'),

   #edit staff info
    url(r'^edit_staffinfo/(?P<id>\d+)/$','eLeave.views.edit_staffinfo'),
    url(r'^edit_stafftraining/(?P<id>\d+)/$','eLeave.views.edit_stafftraining'),
    url(r'^edit_staffemployment/(?P<id>\d+)/$','eLeave.views.edit_staffemployment'),

   #export csv files
   #url(r'^export_to_csv_file/$','eLeave.views.export_to_csv_file'),
  # url(r'^training_history_csv/$','eLeave.views.training_history_csv'),
  # url(r'^training_history_csv/$','eLeave.views.training_history_csv'),
   url(r'^staff_info_csv/$','eLeave.views.staff_info_csv'),
   url(r'^leave_info_csv/$','eLeave.views.leave_info_csv'),

#leave balance
   url('^leave_balance/$','leavebalance.views.leave_balance'),
   url(r'^displaycurrentbalance/$','leavebalance.views.displaycurrentbalance'),
   url(r'^departments/$','leavebalance.views.departments'),
   url(r'^importleavebalance/$','leavebalance.views.importleavebalance'),
   url(r'^leave_balance_calculator/(?P<id>\d+)/$','leavebalance.views.leave_balance_calculator'),
  # url(r'^sum_leavebalance/$','leavebalance.views.sum_leavebalance'),
  # url(r'^kalpeau_leavebalance/$','leavebalance.views.kalpeau_leavebalance'),
   url(r'^departments/$','leavebalance.views.departments'),
   url(r'^fmkd_currentleave_balance/$','leavebalance.views.fmkd_currentleave_balance'),
   url(r'^rshd_currentleave_balance/$','leavebalance.views.rshd_currentleave_balance'),
   url(r'^acsd_currentleave_balace/$','leavebalance.views.acsd_currentleave_balace'),
   url(r'^fisd_currentleave_balance/$','leavebalance.views.fisd_currentleave_balance'),
   url(r'^csd_currentleave_balance/$','leavebalance.views.csd_currentleave_balance'),



           #leave history
            url(r'^leavehistory/$','leavebalance.views.leavehistory'),
                     url(r'^download_history/$','leavebalance.views.download_history'),


#accounts encashment
url(r'^encash/$', 'leavebalance.views.encash'),
url(r'^encashment/$', 'leavebalance.views.encashment'),
url(r'^encashment_display/$', 'leavebalance.views.encashment_display'),
url(r'^leave_payout/$', 'leavebalance.views.leave_payout'),
url(r'^leave_encashment_calculator/(?P<id>\d+)/$', 'leavebalance.views.leave_encashment_calculator'),
url(r'^accounts/$', 'leavebalance.views.accounts'),


   #FMKD leave Balance
  url(r'^Albert_leavebalance/$','leavebalance.views.Albert_leavebalance'),
  url(r'^Alison_leavebalance/$','leavebalance.views.Alison_leavebalance'),
  url(r'^Frederic_leavebalance/$','leavebalance.views.Frederic_leavebalance'),
  url(r'^Johncy_leavebalance/$','leavebalance.views.Johncy_leavebalance'),
  url(r'^Lynrose_leavebalance/$','leavebalance.views.Lynrose_leavebalance'),
  url(r'^philip_leavebalance/$','leavebalance.views.philip_leavebalance'),
  url(r'^robinsion_leavebalance/$','leavebalance.views.robinsion_leavebalance'),
  url(r'^Tonny_leavebalance/$','leavebalance.views.Tonny_leavebalance'),
  url(r'^Simon_leavebalance/$','leavebalance.views.Simon_leavebalance'),
  url(r'^Vicky_leavebalance/$','leavebalance.views.Vicky_leavebalance'),

  #CSD leave Balance
  url(r'^Alick_leavebalance/$','leavebalance.views.Alick_leavebalance'),
  url(r'^Ambata_leavebalance/$','leavebalance.views.Ambata_leavebalance'),
  url(r'^Betty_leavebalance/$','leavebalance.views.Betty_leavebalance'),
  url(r'^Charlie_leavebalance/$','leavebalance.views.Charlie_leavebalance'),
  url(r'^CharlieBeru_leavebalance/$','leavebalance.views.CharlieBeru_leavebalance'),
  url(r'^Daffodil_leavebalance/$','leavebalance.views.Daffodil_leavebalance'),
  url(r'^Fred_leavebalance/$','leavebalance.views.Fred_leavebalance'),
  url(r'^Iven_leavebalance/$','leavebalance.views.Iven_leavebalance'),
  url(r'^Jessica_leavebalance/$','leavebalance.views.Jessica_leavebalance'),
  url(r'^Joseth_leavebalance/$','leavebalance.views.Joseth_leavebalance'),
   url(r'^keith_leavebalance/$','leavebalance.views.keith_leavebalance'),
    url(r'^ken_leavebalance/$','leavebalance.views.ken_leavebalance'),
     url(r'^Lonneth_leavebalance/$','leavebalance.views.Lonneth_leavebalance'),
      url(r'^Lillian_leavebalance/$','leavebalance.views.Lillian_leavebalance'),
       url(r'^Nelson_leavebalance/$','leavebalance.views.Nelson_leavebalance'),
        url(r'^Nancys_leavebalance/$','leavebalance.views.Nancys_leavebalance'),
         url(r'^Pakoa_leavebalance/$','leavebalance.views.Pakoa_leavebalance'),
          url(r'^Philip_leavebalance/$','leavebalance.views.Philip_leavebalance'),
           url(r'^Rebeca_leavebalance/$','leavebalance.views.Rebeca_leavebalance'),
            url(r'^Thevfa_leavebalance/$','leavebalance.views.Thevfa_leavebalance'),
             #url(r'^Iven_leavebalance/$','leavebalance.views.Iven_leavebalance'),


 #ACSD leave Balance
                  url(r'^Beneth_leavebalance/$','leavebalance.views.Beneth_leavebalance'),
              url(r'^Carolyn_leavebalance/$','leavebalance.views.Carolyn_leavebalance'),
            url(r'^Derek_leavebalance/$','leavebalance.views.Derek_leavebalance'),
          url(r'^Florinda_leavebalance/$','leavebalance.views.Florinda_leavebalance'),
        url(r'^Juanita_leavebalance/$','leavebalance.views.Juanita_leavebalance'),
      url(r'^Julia_leavebalance/$','leavebalance.views.Julia_leavebalance'),
    url(r'^Kenny_leavebalance/$','leavebalance.views.Kenny_leavebalance'),
  url(r'^Kensen_leavebalance/$','leavebalance.views.Kensen_leavebalance'),
    url(r'^Ruth_leavebalance/$','leavebalance.views.Ruth_leavebalance'),
      url(r'^Sussie_leavebalance/$','leavebalance.views.Sussie_leavebalance'),
        url(r'^Shirly_leavebalance/$','leavebalance.views.Shirly_leavebalance'),
            url(r'^heva_leavebalance/$','leavebalance.views.heva_leavebalance'),
            url(r'^heva_leavebalance1/$','leavebalance.views.heva_leavebalance1'),
                url(r'^Melonnie_leavebalance/$','leavebalance.views.Melonnie_leavebalance'),
                url(r'^Melonnie_leavebalance1/$','leavebalance.views.Melonnie_leavebalance1'),
                url(r'^Semu_leavebalance/$','leavebalance.views.Semu_leavebalance'),
                url(r'^semu_leavebalance1/$','leavebalance.views.semu_leavebalance1'),
                url(r'^Kasaia_leavebalance/$','leavebalance.views.Kasaia_leavebalance'),
                url(r'^Kasaia_leavebalance1/$','leavebalance.views.Kasaia_leavebalance1'),
                url(r'^Leinasei_leavebalance/$','leavebalance.views.Leinasei_leavebalance'),
                url(r'^Leinasei_leavebalance1/$','leavebalance.views.Leinasei_leavebalance1'),
                url(r'^Haggai_leavebalance/$','leavebalance.views.Haggai_leavebalance'),
                url(r'^Haggai_leavebalance1/$','leavebalance.views.Haggai_leavebalance1'),


#FISD Leave Balance


                  url(r'^Alex_leavebalance/$','leavebalance.views.Alex_leavebalance'),
              url(r'^Florinda_leavebalancefisd/$','leavebalance.views.Florinda_leavebalancefisd'),
            url(r'^Gloria_leavebalance/$','leavebalance.views.Gloria_leavebalance'),
          url(r'^Holyoake_leavebalance/$','leavebalance.views.Holyoake_leavebalance'),
        url(r'^John_leavebalance/$','leavebalance.views.John_leavebalance'),
      url(r'^Jenny_leavebalance/$','leavebalance.views.Jenny_leavebalance'),
    url(r'^Marinet_leavebalance/$','leavebalance.views.Marinet_leavebalance'),
  url(r'^MMark_leavebalance/$','leavebalance.views.MMark_leavebalance'),
    url(r'^Nancy_leavebalance/$','leavebalance.views.Nancy_leavebalance'),
      url(r'^Noel_leavebalance/$','leavebalance.views.Noel_leavebalance'),
        url(r'^Noelyn_leavebalance/$','leavebalance.views.Noelyn_leavebalance'),



#check balance Gov office
url(r'^Gov_aut_check_bal/$','leavebalance.views.Gov_aut_check_bal'),
url(r'^kalpeau_leavebalance1/$','leavebalance.views.kalpeau_leavebalance1'),
url(r'^Tabe_leavebalance1/$','leavebalance.views.Tabe_leavebalance1'),
url(r'^Tom_leavebalance1/$','leavebalance.views.Tom_leavebalance1'),
url(r'^Governor_leavebalance1/$','leavebalance.views.Governor_leavebalance1'),
url(r'^deputyGovernor_leavebalance1/$','leavebalance.views.deputyGovernor_leavebalance1'),
url(r'^Michael_leavebalance1/$','leavebalance.views.Michael_leavebalance1'),
url(r'^Linnes_leavebalance1/$','leavebalance.views.Linnes_leavebalance1'),
url(r'^Branan_leavebalance1/$','leavebalance.views.Branan_leavebalance1'),
url(r'^andrea_leavebalance1/$','leavebalance.views.andrea_leavebalance1'),
url(r'^andrea_leavebalance1/$','leavebalance.views.andrea_leavebalance1'),
url(r'^sum_leavebalance1/$','leavebalance.views.sum_leavebalance1'),


#check balance FMD office
url(r'^fmd_aut_check_bal/$','leavebalance.views.fmd_aut_check_bal'),
url(r'^Albert_leavebalance1/$','leavebalance.views.Albert_leavebalance1'),
url(r'^Alison_leavebalance1/$','leavebalance.views.Alison_leavebalance1'),
url(r'^Frederic_leavebalance1/$','leavebalance.views.Frederic_leavebalance1'),
url(r'^Johncy_leavebalance1/$','leavebalance.views.Johncy_leavebalance1'),
url(r'^Lynrose_leavebalance1/$','leavebalance.views.Lynrose_leavebalance1'),
url(r'^philip_leavebalance1/$','leavebalance.views.philip_leavebalance1'),
url(r'^Tonny_leavebalance1/$','leavebalance.views.Tonny_leavebalance1'),
url(r'^Vicky_leavebalance1/$','leavebalance.views.Vicky_leavebalance1'),


#check balance CSD office
url(r'^csd_aut_check_bal/$','leavebalance.views.csd_aut_check_bal'),
url(r'^Alick_leavebalance1/$','leavebalance.views.Alick_leavebalance1'),
url(r'^Ambata_leavebalance1/$','leavebalance.views.Ambata_leavebalance1'),
        url(r'^Betty_leavebalance1/$','leavebalance.views.Betty_leavebalance1'),
        url(r'^Charlie_leavebalance1/$','leavebalance.views.Charlie_leavebalance1'),
        url(r'^CharlieBeru_leavebalance1/$','leavebalance.views.CharlieBeru_leavebalance1'),
url(r'^Daffodil_leavebalance1/$','leavebalance.views.Daffodil_leavebalance1'),
url(r'^Fred_leavebalance1/$','leavebalance.views.Fred_leavebalance1'),
url(r'^Iven_leavebalance1/$','leavebalance.views.Iven_leavebalance1'),
url(r'^Jessica_leavebalance1/$','leavebalance.views.Jessica_leavebalance1'),
     url(r'^Joseth_leavebalance1/$','leavebalance.views.Joseth_leavebalance1'),
      url(r'^keith_leavebalance1/$','leavebalance.views.keith_leavebalance1'),
         url(r'^ken_leavebalance1/$','leavebalance.views.ken_leavebalance1'),
            url(r'^Lonneth_leavebalance1/$','leavebalance.views.Lonneth_leavebalance1'),
              url(r'^Lillian_leavebalance1/$','leavebalance.views.Lillian_leavebalance1'),
            url(r'^Nelson_leavebalance1/$','leavebalance.views.Nelson_leavebalance1'),
url(r'^Nancy_leavebalance1/$','leavebalance.views.Nancy_leavebalance1'),
url(r'^Pakoa_leavebalance1/$','leavebalance.views.Pakoa_leavebalance1'),
url(r'^Philip_leavebalance1/$','leavebalance.views.Philip_leavebalance1'),
url(r'^Rebeca_leavebalance1/$','leavebalance.views.Rebeca_leavebalance1'),
url(r'^Thevfa_leavebalance1/$','leavebalance.views.Thevfa_leavebalance1'),

#check balance  ACSD office
url(r'^acsd_aut_check_bal/$','leavebalance.views.acsd_aut_check_bal'),
url(r'^Beneth_leavebalance1/$','leavebalance.views.Beneth_leavebalance1'),
url(r'^Carolyn_leavebalance1/$','leavebalance.views.Carolyn_leavebalance1'),
url(r'^Derek_leavebalance1/$','leavebalance.views.Derek_leavebalance1'),
url(r'^Florinda_leavebalance1/$','leavebalance.views.Florinda_leavebalance1'),
url(r'^Juanita_leavebalance1/$','leavebalance.views.Juanita_leavebalance1'),
url(r'^Julia_leavebalance1/$','leavebalance.views.Julia_leavebalance1'),
url(r'^Kenny_leavebalance1/$','leavebalance.views.Kenny_leavebalance1'),
url(r'^Kensen_leavebalance1/$','leavebalance.views.Kensen_leavebalance1'),
url(r'^Ruth_leavebalance1/$','leavebalance.views.Ruth_leavebalance1'),
url(r'^Sussie_leavebalance1/$','leavebalance.views.Sussie_leavebalance1'),
url(r'Shirly_leavebalance1/$','leavebalance.views.Shirly_leavebalance1'),




# Hr office upload file
url(r'^uploadfunc/$','leavebalance.views.uploadfunc'),
#url(r'^displayfile/$','leavebalance.views.displayfile'),

#Unit manger to approve leave test
url(r'^department_to_approve_leavetest/$','eLeave.views.department_to_approve_leavetest'),
url(r'^department_to_approve_leavefmd/$','eLeave.views.department_to_approve_leavefmd'),
url(r'^department_to_approve_leavecsd/$','eLeave.views.department_to_approve_leavecsd'),
url(r'^department_to_approve_leaveacsd/$','eLeave.views.department_to_approve_leaveacsd'),
url(r'^department_to_approve_leavearsd/$','eLeave.views.department_to_approve_leavearsd'),
url(r'^department_to_approve_leaveafsd/$','eLeave.views.department_to_approve_leaveafsd'),
url(r'^unit_department_to_approve_leave/$','eLeave.views.unit_department_to_approve_leave'),


#unit Director to approve leave

url(r'^department_to_approve_leavegov1/$','eLeave.views.department_to_approve_leavegov1'),
url(r'^Gov111/$','eLeave.views.Gov111'),
url(r'^Gov11approved/$','eLeave.views.Gov11approved'),
url(r'^department_to_approve_leavefmd1/$','eLeave.views.department_to_approve_leavefmd1'),
url(r'^fmd111/$','eLeave.views.fmd111'),
url(r'^fmd11approved/$','eLeave.views.fmd11approved'),
url(r'^department_to_approve_leavecsd1/$','eLeave.views.department_to_approve_leavecsd1'),
url(r'^csd111/$','eLeave.views.csd111'),
url(r'^csd11approved/$','eLeave.views.csd11approved'),
url(r'^department_to_approve_leaveacsd1/$','eLeave.views.department_to_approve_leaveacsd1'),
url(r'^acsd111/$','eLeave.views.acsd111'),
url(r'^acsd11approved/$','eLeave.views.acsd11approved'),
url(r'^department_to_approve_leavearsd1/$','eLeave.views.department_to_approve_leavearsd1'),
url(r'^rsd111/$','eLeave.views.rsd111'),
url(r'^rsd11approved/$','eLeave.views.rsd11approved'),
url(r'^department_to_approve_leaveafisd1/$','eLeave.views.department_to_approve_leaveafisd1'),
url(r'^fisd111/$','eLeave.views.fisd111'),
url(r'^fisd11approved/$','eLeave.views.fisd11approved'),

url(r'^unit_director_to_approve_leave/$','eLeave.views.unit_director_to_approve_leave'),

#write to database link
url(r'^write_todatabase/$','eLeave.views.write_todatabase'),

#hr tracking all leave
url(r'^leaveapp/$','eLeave.views.leaveapp'),

#process leave balance
url(r'^process_Leaveform/(?P<id>\d+)/$','eLeave.views.process_Leaveform'),

#process leaves
url(r'^display_processbal/$','eLeave.views.display_processbal'),
url(r'^display_processfisd/$','eLeave.views.display_processfisd'),
url(r'^display_processrsd/$','eLeave.views.display_processrsd'),
url(r'^display_processcsd/$','eLeave.views.display_processcsd'),
url(r'^display_processacsd/$','eLeave.views.display_processacsd'),
url(r'^display_processfmd/$','eLeave.views.display_processfmd'),

#rejected leaves
url(r'^rejected_leaves/$','eLeave.views.rejected_leaves'),


)
