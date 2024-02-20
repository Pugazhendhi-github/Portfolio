from django.contrib import admin
from .models import PortfolioForm

class ContactAdmin(admin.ModelAdmin):
    list = [ 'name' , 'contactmail' , 'message' ]
    
admin.site.register(PortfolioForm, ContactAdmin)
