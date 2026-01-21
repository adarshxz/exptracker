from django.db import models

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Entertainment', 'Entertainment'),
        ('Shopping', 'Shopping'),
        ('Utilities', 'Utilities'),
        ('Other', 'Other'),
    ]

    PAYMENT_CHOICES = [
        ('Cash', 'Cash'),
        ('Credit Card', 'Credit Card'),
        ('Debit Card', 'Debit Card'),
        ('UPI', 'UPI'),
        ('Net Banking', 'Net Banking'),
    ]

    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default='Cash')

    def __str__(self):
        return f"{self.title} - {self.amount}"

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, default="Expense Tracker")
    site_description = models.TextField(blank=True)
    contact_email = models.EmailField(blank=True)
    footer_text = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name_plural = "Site Settings"
