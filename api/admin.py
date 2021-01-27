from django.contrib import admin
from api.models import Company, Employee


class ApiCompanyAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    fields = ('id', 'name')


class ApiEmployeeAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    fields = ('id', 'last_name', 'first_name', 'middle_name', 'company')
    list_filter = ('company',)


admin.site.register(Company, ApiCompanyAdmin)
admin.site.register(Employee, ApiEmployeeAdmin)
