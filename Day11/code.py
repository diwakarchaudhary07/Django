# ✅ Day  11 :- CRUD Operation Update And Delete.

# # # Delete Data
# def delete_student(request, id):
#     data = Student.objects.get(id=id)
#     data.delete()
#     return redirect('student_list')


# # # Update Data
# def edit_student(request, id):
#     data = Student.objects.get(id=id)


#     if request.method == 'POST':
#         data.std_name = request.POST['name']
#         data.std_roll = request.POST['roll']
#         data.std_email = request.POST['email']
#         data.std_city = request.POST['city']


#         if request.FILES.get('image'):
#             data.std_image = request.FILES['image']


#         data.save()
#         return redirect('student_list')


#     return render(request, 'edit.html', {'data': data})





