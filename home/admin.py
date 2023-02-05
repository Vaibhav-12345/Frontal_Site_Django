from django.contrib import admin

# Register your models here.
from home.models import contactform
from home.models import carousel
from home.models import defaultcarousel
from home.models import servicecard



class card(admin.ModelAdmin):
    list_display=('image','imgtitle',' imginto')
    

admin.site.register(contactform)
admin.site.register(carousel)
admin.site.register(defaultcarousel)
admin.site.register(servicecard)
