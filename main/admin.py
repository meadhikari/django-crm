# -*- coding: utf-8 -*-

from django.contrib import admin
from main.models import Customer
from main.models import Payment
from rangefilter.filter import DateRangeFilter

from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from main.tools.dateconverter import NepaliDateConverter
from main.actions import export_as_csv_action
admin.site.unregister(User)
admin.site.unregister(Group)
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','address','margh','house_no','barga_fit','land_kitta_number','land_area','monthly_fee','chetra','batoko_kisim','ghar_ko_kisim',)
    search_fields = ['name','address','margh','house_no','barga_fit','land_kitta_number','land_area','monthly_fee','chetra','batoko_kisim','ghar_ko_kisim',]
    list_filter = ('chetra','batoko_kisim','ghar_ko_kisim',)
admin.site.register(Customer, CustomerAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('customer','rasid_number','amount','nepali_date','remarks',)
    search_fields = ['customer','rasid_number']
    raw_id_fields = ("customer",)
    list_filter = (
        ('date', DateRangeFilter),
    )

    def nepali_date(self, obj):

        date = obj.date
        year = date.year
        month = date.month
        day = date.day
        converter = NepaliDateConverter()
        date = converter.ad2bs((year, month, day))
        return converter.format_date(date, target="np")

    actions = [export_as_csv_action("CSV Export", fields=['customer','rasid_number','amount'])]
    nepali_date.short_description = u"मिति"
admin.site.register(Payment, PaymentAdmin)
