from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Parent
from django.contrib import messages
from datetime import datetime

# Create your views here.
def student_list(request):
    student_list = Student.objects.select_related('parent').all()
    context = {
        'student': student_list
    }
    return render(request, 'students/students.html', context)

def student_details(request, slug):
    student = Student.objects.select_related('parent').get(slug=slug)

    context = {
        'student': student
    }
    return render(request, 'students/student-details.html', context)

def add_student(request):
    if request.method == "POST":
        # Handle form submission
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_id = request.POST.get('student_id')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        student_classes = request.POST.get('student_classes')
        mobile_number = request.POST.get('mobile_number')
        joining_date = request.POST.get('joining_date')
        admission_number = request.POST.get('admission_number')
        section = request.POST.get('section')
        religion = request.POST.get('religion')
        image = request.FILES.get('image')

        #Parents section handling
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_mobile = request.POST.get('father_mobile')
        father_email = request.POST.get('father_email')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        mother_mobile = request.POST.get('mother_mobile')
        mother_email = request.POST.get('mother_email')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')

        # save the parents section
        parent = Parent.objects.create(
            father_name=father_name,
            father_ocupation=father_occupation,
            father_mobile=father_mobile,
            father_email=father_email,
            mother_name=mother_name,
            mother_ocupation=mother_occupation,
            mother_mobile=mother_mobile,
            mother_email=mother_email,
            present_address=present_address,
            permanent_address=permanent_address
        )

        # save the student section
        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            student_id=student_id,
            date_of_birth=date_of_birth,
            gender=gender,
            student_class=student_classes,
            mobile_number=mobile_number,
            joining_date=joining_date,
            admission_number=admission_number,
            section=section,
            religion=religion,
            image=image,
            parent=parent
        )
        messages.success(request, "Student added successfully.")
        return render(request, 'Home/index.html')
    return render(request, 'students/add-student.html')

def edit_student(request, slug):
    student = get_object_or_404(Student, slug=slug)
    # Use getattr to safely get parent if it's a ForeignKey/OneToOne
    parent = getattr(student, 'parent', None) 

    if request.method == "POST":
        # Update Student Fields (Note: No commas at the end!)
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.student_id = request.POST.get('student_id')
        # Inside your edit_student view, under request.method == "POST":
        date_of_birth_str = request.POST.get('date_of_birth')
        joining_date_str = request.POST.get('joining_date')
        try:
            # Adjust the format string '%b. %d, %Y' to match exactly what your form sends
            # %b is short month (Nov), %d is day (5), %Y is year (1998)
            if date_of_birth_str:
                student.date_of_birth = datetime.strptime(date_of_birth_str.replace('“', '').replace('”', ''), '%b. %d, %Y').date()
            
            if joining_date_str:
                student.joining_date = datetime.strptime(joining_date_str.replace('“', '').replace('”', ''), '%b. %d, %Y').date()
        except ValueError:
            # Fallback: if it's already YYYY-MM-DD or in a different format
            student.date_of_birth = date_of_birth_str 
            student.joining_date = joining_date_str
        
        student.gender = request.POST.get('gender')
        student.student_class = request.POST.get('student_class')
        student.mobile_number = request.POST.get('mobile_number')
        student.admission_number = request.POST.get('admission_number')
        student.section = request.POST.get('section')
        student.religion = request.POST.get('religion')

        # Only update image if a new one was uploaded
        new_image = request.FILES.get('image')
        if new_image:
            student.image = new_image
        
        student.save()

        # Update Parent Fields (if parent exists)
        if parent:
            parent.father_name = request.POST.get('father_name')
            parent.father_occupation = request.POST.get('father_occupation')
            parent.father_mobile = request.POST.get('father_mobile')
            parent.father_email = request.POST.get('father_email')
            parent.mother_name = request.POST.get('mother_name')
            parent.mother_occupation = request.POST.get('mother_occupation')
            parent.mother_mobile = request.POST.get('mother_mobile')
            parent.mother_email = request.POST.get('mother_email')
            parent.permanent_address = request.POST.get('permanent_address')
            parent.present_address = request.POST.get('present_address')
            parent.save()

        # Redirect to a success page or the student list
        return redirect('student_list') 

    # Context for the GET request (initial form load)
    context = {
        'student': student,
        'parent': parent
    }
    return render(request, 'students/edit-student.html', context)

def student_dashboard(request):
    return render(request, 'students/student-dashboard.html')

def delete_student(request, slug):
    student = get_object_or_404(Student, slug=slug)
    student.delete()
    messages.success(request, "Student deleted successfully.")
    return render(request, 'students/students.html')