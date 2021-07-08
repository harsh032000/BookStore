from django.db.models import fields
import django_filters

from .models import *

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['name', 'author']