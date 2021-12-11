from django.contrib import admin
from .models import Portal
from .models import Categories


#class AppAdmin(admin.ModelAdmin):
 #   list_display = ('title', 'author', 'publish', 'status')
  #  list_filter = ('status', 'publish', 'author')
   # search_fields = ('title', 'body')
    #raw_id_fields = ('author',)
    #date_hierarchy = 'publish'
    #ordering = ['status', 'publish']


admin.site.register(Portal)
admin.site.register(Categories)


