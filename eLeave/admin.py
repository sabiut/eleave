from django.contrib import admin
#from eLeave.models import staff
#from eLeave.models import leave
from eLeave.models import new_staff
from eLeave.models import newleave
from eLeave.models import training
from eLeave.models import employment_history


# Register your models here.
#admin.site.register(staff)
#admin.site.register(leave)
admin.site.register(new_staff)
admin.site.register(newleave)
admin.site.register(training)
admin.site.register(employment_history)
