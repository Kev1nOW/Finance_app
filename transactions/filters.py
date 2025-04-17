import django_filters
from django import forms
from .models import Record, Status, Type, Category, Subcategory


class RecordFilter(django_filters.FilterSet):
    date_from = django_filters.DateFilter(
        field_name='date', 
        lookup_expr='gte', 
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    date_to = django_filters.DateFilter(
        field_name='date', 
        lookup_expr='lte', 
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    operations_type = django_filters.ModelChoiceFilter(
        queryset=Type.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    subcategory = django_filters.ModelChoiceFilter(
        queryset=Subcategory.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Record
        fields = ['date_from', 'date_to', 'status', 'operations_type', 'category', 'subcategory']


