from django.db import models
import datetime
from django.urls import reverse

makes = (
    ('bmw', 'BMW'),
    ('merc', 'MERCEDES'),
    ('lexus', 'LEXUS'),
    ('sub', 'SUBARU'),
    ('toy', 'TOYOTA')
)

DESIGN_CHOICES = (
    ('suv', 'SUV'),
    ('4x4', '4X4'),
    ('saloon', 'SALOON'),
    ('supercar', 'SUPERCAR')
)


class Category(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(choices=makes, max_length=100, default='toy')
    description = models.TextField(max_length=500)
    design = models.CharField(choices=DESIGN_CHOICES, default='saloon', max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name', 'category']
        verbose_name_plural = "Categories"



class Car(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category)
    mileage = models.IntegerField()
    car_design = models.CharField(choices=DESIGN_CHOICES, default='', max_length=100)
    image = models.ImageField(upload_to='documents/')   # files will be automatically uploaded to MEDIA_ROOT/documents
    rate = models.IntegerField()

    is_available = models.NullBooleanField(blank=True, null=True)

    def __str__(self):
        return self.name, [self.category]

    def get_absolute_url(self):
        return reverse('car-details', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['name', 'category']
        verbose_name_plural = "Cars"


class Customer(models.Model):
    id_number = models.CharField(max_length=30, blank=True, null=True)
    passport_number = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name, [self.phone_num]

    def get_absolute_url(self):
        return reverse('customer-details', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['name', 'id_number', 'passport_number']
        verbose_name_plural = "Customers"


class Booking(models.Model):
    customer = models.ForeignKey(Customer)
    car = models.ForeignKey(Car, blank=True, null=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    approved = models.BooleanField()
    book_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['customer', 'approved']
        verbose_name_plural = "Bookings"
    



