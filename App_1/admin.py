from django.contrib import admin
from App_1.models import AccessRecord, Topic, Webpage, for_user

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(for_user)
