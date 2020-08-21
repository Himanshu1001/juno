from django.contrib import admin
from .models import PhoneOTP, UserTasks, User, Custom_User, Challanges, Content

# Register your models here.
admin.site.site_header = '7C Admin Dashboard'                   
admin.site.index_title = '7C Admin Dashboard'                
admin.site.site_title = 'Welcome to 7C Admin Dashboard'

class PhoneOtpAdmin(admin.ModelAdmin):
    pass

admin.site.register(PhoneOTP, PhoneOtpAdmin)

class UserTasksAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserTasks, UserTasksAdmin)

class Custom_UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Custom_User, Custom_UserAdmin)

class ChallangesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Challanges, ChallangesAdmin)

class ContentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Content, ContentAdmin)