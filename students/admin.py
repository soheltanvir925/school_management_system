from django.contrib import admin
from .models import Parent, Student

# Register your models here.
@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('father_name', 'mother_name', 'father_mobile', 'mother_mobile')
    search_fields = ('father_name', 'mother_name', 'father_email', 'mother_email')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_id', 'date_of_birth', 'gender', 'student_class', 'mobile_number', 'joining_date', 'section', 'admission_number')
    search_fields = ('first_name', 'last_name', 'student_id', 'admission_number', 'student_class')
    list_filter = ('gender', 'student_class', 'section')
    readonly_fields = ('image',)
