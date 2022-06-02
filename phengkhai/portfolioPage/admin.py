from django.contrib import admin

# Register your models here.
from .models import Projects,Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'desc']
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Projects)
admin.site.register(Category)