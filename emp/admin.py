from django.contrib import admin

from emp.models import Emp, Testimonial

# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display=('name','working','emp_id','phone')
    list_editable=('working','emp_id')
    search_fields=('name',)
    list_filter=('working',)





admin.site.register(Emp,EmpAdmin)
admin.site.register(Testimonial)




'''
maheshpatil
mahesh@gmail.com
Mahesh@123
'''