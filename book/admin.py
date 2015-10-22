from django.contrib import admin

# Register your models here.
from .models import Publisher,Author,Book


class PublisherAdmin(admin.ModelAdmin):
	list_display = ('name','address','city')
	search_fields = ('name','city')
	list_filter = ('name',)
	ordering = ("-name",)
	fields = ('city','name')

admin.site.register(Publisher,PublisherAdmin)


admin.site.register(Author)
admin.site.register(Book)
