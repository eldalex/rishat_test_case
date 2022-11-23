from django.contrib import admin
from .models import Item , Order, OrderDetail,Discount, Tax

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display =('id','name','description','price')

class OrderAdmin(admin.ModelAdmin):
    list_display =('id','odrer_dt','order_name','order_discount')

class OrderDetailAdmin(admin.ModelAdmin):
    list_display =('id','detail_binding','item_binding','item_count','order_dt',)
    list_filter = ('detail_binding',)



admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(Discount)
admin.site.register(Tax)

