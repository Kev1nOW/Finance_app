from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Record, Status, Type, Category, Subcategory
from .forms import RecordForm, StatusForm, TypeForm, CategoryForm, SubcategoryForm
from .filters import RecordFilter

# Create your views here.

# Представления для записей о ДДС
class RecordListView(ListView):
    model = Record
    template_name = 'transactions/record_list.html'
    context_object_name = 'records'
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем фильтр
        record_filter = RecordFilter(self.request.GET, queryset=self.get_queryset())
        context['filter'] = record_filter
        context['records'] = record_filter.qs
        return context

class RecordCreateView(CreateView):
    model = Record
    form_class = RecordForm
    template_name = 'transactions/record_form.html'
    success_url = reverse_lazy('transactions:record_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['types'] = Type.objects.all()
        context['categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Запись успешно создана')
        return super().form_valid(form)

class RecordUpdateView(UpdateView):
    model = Record
    form_class = RecordForm
    template_name = 'transactions/record_form.html'
    success_url = reverse_lazy('transactions:record_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['types'] = Type.objects.all()
        context['categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Запись успешно обновлена')
        return super().form_valid(form)

class RecordDeleteView(DeleteView):
    model = Record
    success_url = reverse_lazy('transactions:record_list')
    template_name = 'transactions/record_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Запись успешно удалена')
        return super().delete(request, *args, **kwargs)

# Представления для управления справочниками
class ReferenceListView(ListView):
    model = Status  # Указываем базовую модель
    template_name = 'transactions/references/reference_list.html'
    
    def get_queryset(self):
        return Status.objects.none()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['types'] = Type.objects.all()
        context['categories'] = Category.objects.all()
        context['subcategories'] = Subcategory.objects.all()
        return context

# Представления для Status
class StatusListView(ListView):
    model = Status
    template_name = 'transactions/references/status_list.html'
    context_object_name = 'statuses'

class StatusCreateView(CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'transactions/references/status_form.html'
    success_url = reverse_lazy('transactions:status_list')

    def form_valid(self, form):
        messages.success(self.request, 'Статус успешно создан')
        return super().form_valid(form)

class StatusUpdateView(UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'transactions/references/status_form.html'
    success_url = reverse_lazy('transactions:status_list')

    def form_valid(self, form):
        messages.success(self.request, 'Статус успешно обновлен')
        return super().form_valid(form)

class StatusDeleteView(DeleteView):
    model = Status
    success_url = reverse_lazy('transactions:status_list')
    template_name = 'transactions/references/confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Статус успешно удален')
        return super().delete(request, *args, **kwargs)

# Представления для Type
class TypeListView(ListView):
    model = Type
    template_name = 'transactions/references/type_list.html'
    context_object_name = 'types'

class TypeCreateView(CreateView):
    model = Type
    form_class = TypeForm
    template_name = 'transactions/references/type_form.html'
    success_url = reverse_lazy('transactions:type_list')

    def form_valid(self, form):
        messages.success(self.request, 'Тип операции успешно создан')
        return super().form_valid(form)

class TypeUpdateView(UpdateView):
    model = Type
    form_class = TypeForm
    template_name = 'transactions/references/type_form.html'
    success_url = reverse_lazy('transactions:type_list')

    def form_valid(self, form):
        messages.success(self.request, 'Тип операции успешно обновлен')
        return super().form_valid(form)

class TypeDeleteView(DeleteView):
    model = Type
    success_url = reverse_lazy('transactions:type_list')
    template_name = 'transactions/references/confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Тип операции успешно удален')
        return super().delete(request, *args, **kwargs)

# Представления для Category
class CategoryListView(ListView):
    model = Category
    template_name = 'transactions/references/category_list.html'
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'transactions/references/category_form.html'
    success_url = reverse_lazy('transactions:category_list')

    def form_valid(self, form):
        messages.success(self.request, 'Категория успешно создана')
        return super().form_valid(form)

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'transactions/references/category_form.html'
    success_url = reverse_lazy('transactions:category_list')

    def form_valid(self, form):
        messages.success(self.request, 'Категория успешно обновлена')
        return super().form_valid(form)

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('transactions:category_list')
    template_name = 'transactions/references/confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Категория успешно удалена')
        return super().delete(request, *args, **kwargs)

# Представления для Subcategory
class SubcategoryListView(ListView):
    model = Subcategory
    template_name = 'transactions/references/subcategory_list.html'
    context_object_name = 'subcategories'

class SubcategoryCreateView(CreateView):
    model = Subcategory
    form_class = SubcategoryForm
    template_name = 'transactions/references/subcategory_form.html'
    success_url = reverse_lazy('transactions:subcategory_list')

    def form_valid(self, form):
        messages.success(self.request, 'Подкатегория успешно создана')
        return super().form_valid(form)

class SubcategoryUpdateView(UpdateView):
    model = Subcategory
    form_class = SubcategoryForm
    template_name = 'transactions/references/subcategory_form.html'
    success_url = reverse_lazy('transactions:subcategory_list')

    def form_valid(self, form):
        messages.success(self.request, 'Подкатегория успешно обновлена')
        return super().form_valid(form)

class SubcategoryDeleteView(DeleteView):
    model = Subcategory
    success_url = reverse_lazy('transactions:subcategory_list')
    template_name = 'transactions/references/confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Подкатегория успешно удалена')
        return super().delete(request, *args, **kwargs)

# api для динамической фильтрации
def get_categories_by_type(request):
    type_id = request.GET.get('type_id')
    categories = Category.objects.filter(operations_type_id=type_id).values('id', 'name')
    return JsonResponse(list(categories), safe=False)

def get_subcategories_by_category(request):
    category_id = request.GET.get('category_id')
    subcategories = Subcategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(subcategories), safe=False)
