from django.contrib import admin
from .models import Book,User
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('titulo','author',)
    search_fields = ('titulo',)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display= ('name',)