from django.db import models

# Create your models here.
class Invoice(models.Model):

    class Meta:
        app_label = 'atomic_test'

    customer_id = models.CharField(max_length=30)
    invoice_no = models.CharField(max_length=6, primary_key=True)

class Customer(models.Model):

    class Meta:
        app_label = 'atomic_test'

    id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=30)