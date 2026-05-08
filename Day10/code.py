# ✅ Day  10 :- CRUD Operation.

# # Insert Data
# def add_student(request):
#     if request.method == 'POST':
#         Student.objects.create(
#             std_name=request.POST['name'],
#             std_roll=request.POST['roll'],
#             std_image=request.FILES['image'],
#             std_email=request.POST['email'],
#             std_city=request.POST['city']
#         )
#         return redirect('student_list')
#     return render(request, 'add.html')

# # In This Function We have to firstly check the method is POST or not,
# # if it is POST then we will create a new student object with the data
# #
# #             std_name=request.POST['name'],
# #             std_roll=request.POST['roll'],
# #             std_image=request.FILES['image'],
# #             std_email=request.POST['email'],
# #             std_city=request.POST['city']
# #std_name is the column name in the Student model and request.POST['name']
# # is the name attribute of add student form similarly image email and city
