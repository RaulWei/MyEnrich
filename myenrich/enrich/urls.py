__author__ = 'WMW'

# system import
from django.conf.urls import patterns, include, url

# user import
#from enrich.views import enrich
import enrich.views

urlpatterns = patterns('',
    url(r'^milestone/', enrich.views.enrich),
    url(r'^milestone_history/', enrich.views.milestone_history),
    #url(r'^test', enrich.views.test),
    url(r'^milestone_history_msBox_record', enrich.views.milestone_history_msBox_record),
    url(r'^ajax/deletemiles', enrich.views.delete_milestone), 
    url(r'^ajax/updatemiles', enrich.views.update_milestone),
)

