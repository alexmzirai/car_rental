from django.contrib import admin
from .models import Car, Category, Customer, Booking


class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'mileage', 'car_design', 'rate']
    list_filter = ['is_available', 'category', 'car_design']
    search_fields = ['category', 'car_design']


class BookingAdmin(admin.ModelAdmin):
    list_display = ['customer', 'car', 'start_date', 'end_date', 'approved', 'book_date']
    list_filter = ['customer', 'car', 'approved']
    search_fields = ['customer']
    list_editable = ['approved']    #allows quick selecting of yes or no for selected attributes

    """this section deals with bulk admin actions for multiple booking objects"""
    actions = ['email_customers']

    def email_customers(self, request, queryset):
        for booking in queryset:
            if booking.approved:
                email_body = """Dear {}, we are pleased to inform you that your booking has been approved.
                Thanks.""".format(booking.customer)
            else:
                email_body = """Dear {}, we regret to inform you that we do not have the capacity right now
                to accept your booking. Thanks.""".format(booking.customer)
            print(email_body)
            self.message_user(request, 'Emails sent successfully.') # return a success message to the user

    email_customers.short_description = 'Send email about booking status to customers'

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id_number', 'passport_number', 'name', 'phone_num', 'email']
    list_filter = ['id_number', 'passport_number', 'name', 'phone_num', 'email']
    search_fields = ['phone_num']

admin.site.register(Category)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Customer, CustomerAdmin)









