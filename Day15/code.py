# ✅ Day  15 :- Seeder File And Serch and Filter


# Step 11:- Create a Seed File
#         (App)     students/
#                   │
#                   ├── management/
#                   │   ├── __init__.py
#                   │   └── commands/
#                   │       ├── __init__.py
#                   │       └── seed_students.py


#          students/management/commands/seed_students.py


#          Enter Student Seeded data


# Step 12:- Run Migrations First
#             python manage.py makemigrations
#             python manage.py migrate


# Step 13:- Run Seeder Command
#             python manage.py seed_students


# Step 14:- Add a serching where we can search using name , rool no , city , class
#             Updating View.py and HTML File


# Step 15:- Adding Filter And Paginator
#          Updating View.py and HTML File



# APP Folder => seed_students.py

# from django.core.management.base import BaseCommand
# from managmentsystem.models import Student
# from django.core.files.base import ContentFile
# import random


# class Command(BaseCommand):
#     help = "Seed database with 20 students"


#     def handle(self, *args, **kwargs):


#         students_data = [
#             {
#                 "name": "Aman Sharma",
#                 "student_class": "10th",
#                 "city": "Delhi",
#                 "age": 15,
#                 "address": "Street 1, Delhi",
#                 "roll_no": "R001"
#             },
#             {
#                 "name": "Rahul Verma",
#                 "student_class": "9th",
#                 "city": "Mumbai",
#                 "age": 14,
#                 "address": "Street 2, Mumbai",
#                 "roll_no": "R002"
#             },
#             {
#                 "name": "Priya Singh",
#                 "student_class": "8th",
#                 "city": "Lucknow",
#                 "age": 13,
#                 "address": "Street 3, Lucknow",
#                 "roll_no": "R003"
#             },
#             {
#                 "name": "Neha Gupta",
#                 "student_class": "11th",
#                 "city": "Jaipur",
#                 "age": 16,
#                 "address": "Street 4, Jaipur",
#                 "roll_no": "R004"
#             },
#             {
#                 "name": "Rohit Kumar",
#                 "student_class": "12th",
#                 "city": "Patna",
#                 "age": 17,
#                 "address": "Street 5, Patna",
#                 "roll_no": "R005"
#             },
#             {
#                 "name": "Simran Kaur",
#                 "student_class": "7th",
#                 "city": "Amritsar",
#                 "age": 12,
#                 "address": "Street 6, Amritsar",
#                 "roll_no": "R006"
#             },
#             {
#                 "name": "Karan Mehta",
#                 "student_class": "10th",
#                 "city": "Chandigarh",
#                 "age": 15,
#                 "address": "Street 7, Chandigarh",
#                 "roll_no": "R007"
#             },
#             {
#                 "name": "Anjali Yadav",
#                 "student_class": "9th",
#                 "city": "Kanpur",
#                 "age": 14,
#                 "address": "Street 8, Kanpur",
#                 "roll_no": "R008"
#             },
#             {
#                 "name": "Vikas Sharma",
#                 "student_class": "8th",
#                 "city": "Agra",
#                 "age": 13,
#                 "address": "Street 9, Agra",
#                 "roll_no": "R009"
#             },
#             {
#                 "name": "Pooja Mishra",
#                 "student_class": "11th",
#                 "city": "Bhopal",
#                 "age": 16,
#                 "address": "Street 10, Bhopal",
#                 "roll_no": "R010"
#             },
#             {
#                 "name": "Arjun Patel",
#                 "student_class": "12th",
#                 "city": "Ahmedabad",
#                 "age": 17,
#                 "address": "Street 11, Ahmedabad",
#                 "roll_no": "R011"
#             },
#             {
#                 "name": "Sneha Joshi",
#                 "student_class": "7th",
#                 "city": "Pune",
#                 "age": 12,
#                 "address": "Street 12, Pune",
#                 "roll_no": "R012"
#             },
#             {
#                 "name": "Deepak Roy",
#                 "student_class": "10th",
#                 "city": "Kolkata",
#                 "age": 15,
#                 "address": "Street 13, Kolkata",
#                 "roll_no": "R013"
#             },
#             {
#                 "name": "Meera Das",
#                 "student_class": "9th",
#                 "city": "Guwahati",
#                 "age": 14,
#                 "address": "Street 14, Guwahati",
#                 "roll_no": "R014"
#             },
#             {
#                 "name": "Sahil Khan",
#                 "student_class": "8th",
#                 "city": "Hyderabad",
#                 "age": 13,
#                 "address": "Street 15, Hyderabad",
#                 "roll_no": "R015"
#             },
#             {
#                 "name": "Riya Kapoor",
#                 "student_class": "11th",
#                 "city": "Noida",
#                 "age": 16,
#                 "address": "Street 16, Noida",
#                 "roll_no": "R016"
#             },
#             {
#                 "name": "Yash Thakur",
#                 "student_class": "12th",
#                 "city": "Indore",
#                 "age": 17,
#                 "address": "Street 17, Indore",
#                 "roll_no": "R017"
#             },
#             {
#                 "name": "Tina Arora",
#                 "student_class": "7th",
#                 "city": "Ludhiana",
#                 "age": 12,
#                 "address": "Street 18, Ludhiana",
#                 "roll_no": "R018"
#             },
#             {
#                 "name": "Mohit Jain",
#                 "student_class": "10th",
#                 "city": "Surat",
#                 "age": 15,
#                 "address": "Street 19, Surat",
#                 "roll_no": "R019"
#             },
#             {
#                 "name": "Kavya Rani",
#                 "student_class": "9th",
#                 "city": "Varanasi",
#                 "age": 14,
#                 "address": "Street 20, Varanasi",
#                 "roll_no": "R020"
#             },
#         ]


#         for data in students_data:


#             student, created = Student.objects.get_or_create(
#                 roll_no=data["roll_no"],
#                 defaults={
#                     "name": data["name"],
#                     "student_class": data["student_class"],
#                     "city": data["city"],
#                     "age": data["age"],
#                     "address": data["address"],
#                 }
#             )


#             # Add dummy image
#             if created:
#                 student.image.save(
#                     f"{student.roll_no}.jpg",
#                     ContentFile(b""),
#                     save=True
#                 )


#         self.stdout.write(
#             self.style.SUCCESS("20 Students Seeded Successfully!")
#         )









# APP Folder => Views.py

# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Student
# from django.db.models import Q
# from django.core.paginator import Paginator
# # 📌 READ (List)
# # def student_list(request):
# #     students = Student.objects.all()
# #     return render(request, 'student_list.html', {'students': students})


# # def student_list(request):


# #     query = request.GET.get('q')


# #     students = Student.objects.all()


# #     if query:
# #         students = students.filter(
# #             Q(name__icontains=query) |
# #             Q(roll_no__icontains=query) |
# #             Q(city__icontains=query) |
# #             Q(student_class__icontains=query)
# #         )


# #     context = {
# #         'students': students
# #     }


# #     return render(request, 'student_list.html', context)




# def student_list(request):


#     students = Student.objects.all().order_by('id')


#     # SEARCH
#     query = request.GET.get('q')


#     if query:
#         students = students.filter(
#             Q(name__icontains=query) |
#             Q(roll_no__icontains=query) |
#             Q(city__icontains=query) |
#             Q(student_class__icontains=query)
#         )


#     # FILTER BY NAME
#     name = request.GET.get('name')


#     if name:
#         students = students.filter(name__icontains=name)


#     # FILTER BY ADDRESS
#     address = request.GET.get('address')


#     if address:
#         students = students.filter(address__icontains=address)


#     # FILTER BY DATE
#     date = request.GET.get('date')


#     if date:
#         students = students.filter(created_at=date)


#     # PAGINATION
#     paginator = Paginator(students, 5)


#     page_number = request.GET.get('page')


#     page_obj = paginator.get_page(page_number)


#     context = {
#         'students': page_obj,
#         'page_obj': page_obj,
#     }


#     return render(request, 'student_list.html', context)


# # 📌 CREATE
# def add_student(request):
#     if request.method == "POST":
#         Student.objects.create(
#             name=request.POST.get('name'),
#             student_class=request.POST.get('student_class'),
#             city=request.POST.get('city'),
#             age=request.POST.get('age'),
#             address=request.POST.get('address'),
#             roll_no=request.POST.get('roll_no'),
#             image=request.FILES.get('image')
#         )
#         return redirect('student_list')


#     return render(request, 'add_student.html')




# # 📌 UPDATE
# def update_student(request, id):
#     student = get_object_or_404(Student, id=id)


#     if request.method == "POST":
#         student.name = request.POST.get('name')
#         student.student_class = request.POST.get('student_class')
#         student.city = request.POST.get('city')
#         student.age = request.POST.get('age')
#         student.address = request.POST.get('address')
#         student.roll_no = request.POST.get('roll_no')


#         if request.FILES.get('image'):
#             student.image = request.FILES.get('image')


#         student.save()
#         return redirect('student_list')


#     return render(request, 'update_student.html', {'student': student})




# # 📌 DELETE
# def delete_student(request, id):
#     student = get_object_or_404(Student, id=id)
#     student.delete()
#     return redirect('student_list')






# APP Folder => student_list.html

# {% extends 'base.html' %}


# {% block content %}


# <h2 class="mb-4">Student List</h2>




# <!-- SEARCH + FILTER FORM -->


# <form method="GET" class="mb-4">


#     <div class="row g-2">


#         <!-- SEARCH -->
#         <div class="col-md-3">
#             <input
#                 type="text"
#                 name="q"
#                 class="form-control"
#                 placeholder="Search..."
#                 value="{{ request.GET.q }}"
#             >
#         </div>


#         <!-- NAME FILTER -->
#         <div class="col-md-2">
#             <input
#                 type="text"
#                 name="name"
#                 class="form-control"
#                 placeholder="Filter Name"
#                 value="{{ request.GET.name }}"
#             >
#         </div>


#         <!-- ADDRESS FILTER -->
#         <div class="col-md-2">
#             <input
#                 type="text"
#                 name="address"
#                 class="form-control"
#                 placeholder="Filter Address"
#                 value="{{ request.GET.address }}"
#             >
#         </div>


#         <!-- DATE FILTER -->
#         <div class="col-md-2">
#             <input
#                 type="date"
#                 name="date"
#                 class="form-control"
#                 value="{{ request.GET.date }}"
#             >
#         </div>


#         <!-- FILTER BUTTON -->
#         <div class="col-md-1">
#             <button type="submit"
#                     class="btn btn-primary w-100">
#                 Go
#             </button>
#         </div>


#         <!-- RESET BUTTON -->
#         <div class="col-md-2">
#             <a href="{% url 'student_list' %}"
#                class="btn btn-secondary w-100">
#                Reset
#             </a>
#         </div>


#     </div>


# </form>


# <table class="table table-bordered table-striped">


#     <thead class="table-dark">
#         <tr>
#             <th>Name</th>
#             <th>Class</th>
#             <th>City</th>
#             <th>Age</th>
#             <th>Roll No</th>
#             <th>Image</th>
#             <th>Action</th>
#         </tr>
#     </thead>


#     <tbody>


#     {% for student in students %}
#         <tr>


#             <td>{{ student.name }}</td>
#             <td>{{ student.student_class }}</td>
#             <td>{{ student.city }}</td>
#             <td>{{ student.age }}</td>
#             <td>{{ student.roll_no }}</td>


#             <td>
#                 {% if student.image %}
#                     <img src="{{ student.image.url }}" width="60" class="rounded">
#                 {% endif %}
#             </td>


#             <td>
#                 <a href="{% url 'update_student' student.id %}"
#                    class="btn btn-warning btn-sm">
#                    Edit
#                 </a>


#                 <a href="{% url 'delete_student' student.id %}"
#                    class="btn btn-danger btn-sm">
#                    Delete
#                 </a>
#             </td>


#         </tr>


#     {% empty %}


#         <tr>
#             <td colspan="7" class="text-center">
#                 No Students Found
#             </td>
#         </tr>


#     {% endfor %}


#     </tbody>


# </table>
# <!-- PAGINATION -->


# <nav aria-label="Page navigation">


#     <ul class="pagination justify-content-center">


#         <!-- Previous Button -->
#         {% if page_obj.has_previous %}
#             <li class="page-item">
#                 <a class="page-link"
#                    href="?page={{ page_obj.previous_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}">
#                    Previous
#                 </a>
#             </li>
#         {% endif %}


#         <!-- Page Numbers -->
#         {% for num in page_obj.paginator.page_range %}


#             {% if page_obj.number == num %}


#                 <li class="page-item active">
#                     <span class="page-link">
#                         {{ num }}
#                     </span>
#                 </li>


#             {% else %}


#                 <li class="page-item">
#                     <a class="page-link"
#                        href="?page={{ num }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}">
#                        {{ num }}
#                     </a>
#                 </li>


#             {% endif %}


#         {% endfor %}


#         <!-- Next Button -->
#         {% if page_obj.has_next %}
#             <li class="page-item">
#                 <a class="page-link"
#                    href="?page={{ page_obj.next_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}">
#                    Next
#                 </a>
#             </li>
#         {% endif %}


#     </ul>


# </nav>


# {% endblock %}
