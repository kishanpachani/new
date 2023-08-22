from django.contrib import admin
from .models import Signup
from .models import add
from django.utils.html import format_html
# Register your models here.

admin.site.register(Signup)

class getdata(admin.ModelAdmin):
    def image_tag(self,obj):
        return format_html('<img src={} height="100" weight="100" >'.format(obj.image.url))
    list_display=['id','image_tag','price','created']

admin.site.register(add,getdata)