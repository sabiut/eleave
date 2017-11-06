from django.contrib import admin
from leavebalance.models import leavecurrentbalance
from leavebalance.models import staffencashment
from leavebalance.models import uploadfile

# Register your models here.
admin.site.register(leavecurrentbalance)
admin.site.register(staffencashment)
admin.site.register(uploadfile)
