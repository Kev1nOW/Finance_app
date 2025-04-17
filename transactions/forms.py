from django import forms
from django.core.exceptions import ValidationError
from .models import Record, Status, Type, Category, Subcategory
import datetime

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['date', 'status', 'operations_type', 'category', 'subcategory', 'amount', 'comment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'operations_type': forms.Select(attrs={'class': 'form-control', 'id': 'id_operations_type'}),
            'category': forms.Select(attrs={'class': 'form-control', 'id': 'id_category'}),
            'subcategory': forms.Select(attrs={'class': 'form-control', 'id': 'id_subcategory'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            self.initial['date'] = datetime.date.today()
            
        # Указываем что поля обязательны
        self.fields['status'].required = True
        self.fields['operations_type'].required = True
        self.fields['category'].required = True
        self.fields['subcategory'].required = True
        self.fields['amount'].required = True

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        subcategory = cleaned_data.get('subcategory')
        operations_type = cleaned_data.get('operations_type')

        if subcategory and category and subcategory.category != category:
            raise forms.ValidationError("Подкатегория не относится к выбранной категории!")

        if category and operations_type and category.operations_type != operations_type:
            raise forms.ValidationError("Категория не относится к выбранному типу операции!")
            
        return cleaned_data

# Формы для справочников
class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'operations_type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'operations_type': forms.Select(attrs={'class': 'form-control'})
        }

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        } 