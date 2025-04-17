from django.contrib import admin
from django import forms
from django.urls import path
from django.http import JsonResponse
from .models import Status, Type, Category, Subcategory, Record


class CustomAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('get_subcategories/', self.admin_view(self.get_subcategories)),
            path('get_categories/', self.admin_view(self.get_categories)),
        ]
        return custom_urls + urls
    
    def get_subcategories(self, request):
        category_id = request.GET.get('category_id')
        if category_id:
            subcategories = Subcategory.objects.filter(category_id=category_id).values('id', 'name')
            return JsonResponse(list(subcategories), safe=False)
        return JsonResponse([], safe=False)
    
    def get_categories(self, request):
        operations_type_id = request.GET.get('operations_type')
        if operations_type_id:
            categories = Category.objects.filter(operations_type_id=operations_type_id).values('id', 'name')
            return JsonResponse(list(categories), safe=False)
        return JsonResponse([], safe=False)

admin_site = CustomAdminSite(name='custom_admin')

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'
    
    def clean(self):
        cleaned_data = super().clean()

        category = cleaned_data.get('category')
        subcategory = cleaned_data.get('subcategory')
        operations_type = cleaned_data.get('operations_type')

        if subcategory and subcategory.category != category:
            raise forms.ValidationError("Подкатегория не относится к категории!")

        if category and category.operations_type != operations_type:
            raise forms.ValidationError("Категория не относится к типу!")

# Регистрация моделей в стандартной админке Django
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('date', 'status', 'operations_type', 'category', 'subcategory', 'amount', 'comment')
    list_filter = ('date', 'status', 'operations_type', 'category', 'subcategory') 
    date_hierarchy = 'date'
    search_fields = ('comment',)
    
    class Media:
        js = ('admin/js/record_dynamic.js',)

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'operations_type')
    list_filter = ('operations_type',)
    search_fields = ('name',)

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category', 'category__operations_type')
    search_fields = ('name',)

# Регистрация моделей в кастомной админке
class RecordAdminCustom(RecordAdmin):
    pass

class StatusAdminCustom(StatusAdmin):
    pass

class TypeAdminCustom(TypeAdmin):
    pass

class CategoryAdminCustom(CategoryAdmin):
    pass

class SubcategoryAdminCustom(SubcategoryAdmin):
    pass

admin_site.register(Record, RecordAdminCustom)
admin_site.register(Status, StatusAdminCustom)
admin_site.register(Type, TypeAdminCustom)
admin_site.register(Category, CategoryAdminCustom)
admin_site.register(Subcategory, SubcategoryAdminCustom)


