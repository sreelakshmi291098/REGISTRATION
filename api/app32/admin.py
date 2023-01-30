from django.contrib import admin

# Register your models here.
from app32.models import login,stud_Reg,teach_Reg

admin.site.register(login)
admin.site.register(stud_Reg)
admin.site.register(teach_Reg)