from django.conf.urls import patterns, include, url
from  . import views
from django.contrib import admin


urlpatterns=(

    #Gov office leave balance
       url(r'^sum_leavebalance/$','leavebalance.views.sum_leavebalance'),
       url(r'^kalpeau_leavebalance/$','leavebalance.views.kalpeau_leavebalance'),
       url(r'^Tabe_leavebalance/$','leavebalance.views.Tabe_leavebalance'),
            url(r'^Tom_leavebalance/$','leavebalance.views.Tom_leavebalance'),
                url(r'^Governor_leavebalance/$','leavebalance.views.Governor_leavebalance'),
                    url(r'^deputyGovernor_leavebalance/$','leavebalance.views.deputyGovernor_leavebalance'),
                    url(r'^Michael_leavebalance/$','leavebalance.views.Michael_leavebalance'),
                url(r'^George_leavebalance/$','leavebalance.views.George_leavebalance'),
       url(r'^Branan_leavebalance/$','leavebalance.views.Branan_leavebalance'),
       url(r'^andrea_leavebalance/$','leavebalance.views.andrea_leavebalance'),
       url(r'^Linnes_leavebalance/$','leavebalance.views.Linnes_leavebalance'),
            url(r'^Priscilla_leavebalance1/$','leavebalance.views.Priscilla_leavebalance1'),
                url(r'^Priscilla_leavebalance/$','leavebalance.views.Priscilla_leavebalance'),
	url(r'^Malon_leavebalance/$','leavebalance.views.Malon_leavebalance',name='Malon_leavebalance'),
    url(r'^Malon_leavebalance1/$','leavebalance.views.Malon_leavebalance1',name='Malon_leavebalance1'),



    #csd leave balance
    url(r'^Nauni_leavebalance/$','leavebalance.views.Nauni_leavebalance'),
    url(r'^Nauni_leavebalance1/$','leavebalance.views.Nauni_leavebalance1'),
        url(r'^Ellie_leavebalance/$','leavebalance.views.Ellie_leavebalance'),
        url(r'^Ellie_leavebalance1/$','leavebalance.views.Ellie_leavebalance1'),
                url(r'^Aaron_leavebalance/$','leavebalance.views.Aaron_leavebalance'),
                url(r'^Aaron_leavebalance1/$','leavebalance.views.Aaron_leavebalance1'),
                   

#ACSD leave balance

    url(r'^Sereana_leavebalance/$','leavebalance.views.Sereana_leavebalance'),
    url(r'^Sereana_leavebalance1/$','leavebalance.views.Sereana_leavebalance1'),
        url(r'^Nerry_leavebalance/$','leavebalance.views.Nerry_leavebalance'),
        url(r'^Nerry_leavebalance1/$','leavebalance.views.Nerry_leavebalance1'),
        url(r'^Mesek_leavebalance/$','leavebalance.views.Mesek_leavebalance'),

#RSD leave balance
url(r'^Lynette_leavebalance/$','leavebalance.views.Lynette_leavebalance'),
url(r'^Lynette_leavebalance1/$','leavebalance.views.Lynette_leavebalance1'),


##check balance  RSD office
url(r'^rsd_aut_check_bal/$','leavebalance.views.rsd_aut_check_bal'),
 url(r'^Alumeci_leavebalance1/$','leavebalance.views.Alumeci_leavebalance1'),
url(r'^Alumeci_leavebalance/$','leavebalance.views.Alumeci_leavebalance'),
url(r'^Arnold_leavebalance1/$','leavebalance.views.Arnold_leavebalance1'),
url(r'^Arnold_leavebalance/$','leavebalance.views.Arnold_leavebalance'),
url(r'^cynthia_leavebalance1/$','leavebalance.views.cynthia_leavebalance1'),
url(r'^cynthia_leavebalance/$','leavebalance.views.cynthia_leavebalance'),
url(r'^Fabiano_leavebalance1/$','leavebalance.views.Fabiano_leavebalance1'),
url(r'^Fabiano_leavebalance/$','leavebalance.views.Fabiano_leavebalance'),
url(r'^Jerry_leavebalance1/$','leavebalance.views.Jerry_leavebalance1'),
url(r'^Joyin_leavebalance1/$','leavebalance.views.Joyin_leavebalance1'),
url(r'^Joyin_leavebalance/$','leavebalance.views.Joyin_leavebalance'),
url(r'^Linda_leavebalance1/$','leavebalance.views.Linda_leavebalance1'),
url(r'^Linda_leavebalance/$','leavebalance.views.Linda_leavebalance'),
url(r'^Mark_leavebalance1/$','leavebalance.views.Mark_leavebalance1'),
url(r'^Mark_leavebalance/$','leavebalance.views.Mark_leavebalance'),
url(r'^Pita_leavebalance1/$','leavebalance.views.Pita_leavebalance1'),
url(r'^Pita_leavebalance/$','leavebalance.views.Pita_leavebalance'),
url(r'^Robert_leavebalance1/$','leavebalance.views.Robert_leavebalance1'),
url(r'^Robert_leavebalance/$','leavebalance.views.Robert_leavebalance'),
#url(r'^Victoria_leavebalance1/$','leavebalance.views.Victoria_leavebalance1'),

#check balance  FISD office
                url(r'^fisd_aut_check_bal/$','leavebalance.views.fisd_aut_check_bal'),
                  url(r'^Alex_leavebalance1/$','leavebalance.views.Alex_leavebalance1'),
              url(r'^Florinda_leavebalancefisd1/$','leavebalance.views.Florinda_leavebalancefisd1'),
            url(r'^Gloria_leavebalance1/$','leavebalance.views.Gloria_leavebalance1'),
          url(r'^Holyoake_leavebalance1/$','leavebalance.views.Holyoake_leavebalance1'),
        url(r'^John_leavebalance1/$','leavebalance.views.John_leavebalance1'),
      url(r'^Jenny_leavebalance1/$','leavebalance.views.Jenny_leavebalance1'),
    url(r'^Marinet_leavebalance1/$','leavebalance.views.Marinet_leavebalance1'),
  url(r'^MMark_leavebalance1/$','leavebalance.views.MMark_leavebalance1'),
    url(r'^Nancy_leavebalance1/$','leavebalance.views.Nancy_leavebalance1'),
      url(r'^Noel_leavebalance1/$','leavebalance.views.Noel_leavebalance1'),
        url(r'^Noelyn_leavebalance1/$','leavebalance.views.Noelyn_leavebalance1'),


#FMD leave balance

url(r'^Juliana_leavebalance/$','leavebalance.views.Juliana_leavebalance'),
url(r'^Juliana_leavebalance1/$','leavebalance.views.Juliana_leavebalance1'),


url(r'^mesek_leavebalance1/$','leavebalance.views.mesek_leavebalance1'),

url(r'^Glenda_leavebalance/$','leavebalance.views.Glenda_leavebalance'),



#staff leave balance report
url(r'^staffbalance_report/$','leavebalance.views.staffbalance_report'),
url(r'^viewgov_officebalance/$','leavebalance.views.viewgov_officebalance',name='viewgov_officebalance'),
url(r'^viewfisd_officebalance/$','leavebalance.views.viewfisd_officebalance',name='viewfisd_officebalance'),
url(r'^viewrsd_officebalance/$','leavebalance.views.viewrsd_officebalance',name='viewrsd_officebalance'),
url(r'^viewcsd_officebalance/$','leavebalance.views.viewcsd_officebalance',name='csd_leavebalance'),
url(r'^viewacsd_officebalance/$','leavebalance.views.viewacsd_officebalance',name='acsd_leabebalance'),
url(r'^viewafmd_officebalance/$','leavebalance.views.viewafmd_officebalance',name='fmd_leavebalance'),
#staff balance end


#download balance

url(r'^download_currentstaffbalance/$','leavebalance.views.download_currentstaffbalance',name='downloadbalance'),




    )
