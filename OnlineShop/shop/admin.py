from django.contrib import admin
from .models import Category, Product
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'numbers', 'availabel')
    list_filter = ('availabel', 'created')
    list_editable = ('price', 'availabel')
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('category',)
    actions = ('make_availabel',)

    def make_availabel(self,request,queryset):
        rows = queryset.update(availabel=True)
        self.message_user(request, '{} Updated'.format(rows))

    make_availabel.short_description = 'make all availabel'