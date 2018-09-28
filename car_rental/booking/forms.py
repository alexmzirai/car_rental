from django import forms
from .models import Car, Booking

class CarImageForm(forms.ModelForm):
    class Meta:
            model = Car
            fields = ('image')


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('customer_name', 'start_date', 'end_date', 'approved', 'book_date')

