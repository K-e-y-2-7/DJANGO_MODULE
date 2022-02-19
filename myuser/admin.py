from django.contrib import admin

from logging import Filter
from django.contrib import admin
import myuser.models


@admin.register(myuser.models.MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'birth_date', 'email', 'is_staff', 'date_joined']
    list_filter = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'date_joined']

#MainAdmin pass: adminpassofdb

