from django.contrib import admin
from .models import Expense, SiteSettings

admin.site.register(Expense)
admin.site.register(SiteSettings)
