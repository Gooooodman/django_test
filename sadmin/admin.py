from django.contrib import admin

# Register your models here.
from .models import Assets

# Register your models here.

class AssetsAdmin(admin.ModelAdmin):
	list_display = ('type','name','config_time','status')
	search_fields = ('name','type')
	list_filter = ('type','name')
	date_hierarchy = 'config_time'
	ordering = ("-config_time",)
	fields = ('type','name','scrap','status')

admin.site.register(Assets,AssetsAdmin)









