# ✅ Day  16:- SMTP(Test Mail Sending)

# There are two types of button
#      Form Button => By using This Button We can store some data Usually this button is used in a form
#         example:- <button type="submit" class="btn btn-success">Add Student</button>


#      Redirect Button => By Using This Button We can redirect on any web page.
#         examplle:- <a class="btn btn-outline-light me-2" href="{% url 'student_list' %}">Home</a>


# Step 16:- Making  A Function To Send Test Email
#           Make Changes in settings.py,views.py,url.py and make a HTML Fie Of Email Sent Message


# Step 17:- Settings.py
#         # Email settings
#         EMAIL_HOST = 'smtp.gmail.com'
#         EMAIL_PORT = 587
#         EMAIL_HOST_USER = 'tridevx9@gmail.com'
#         EMAIL_HOST_PASSWORD = 'ngzf ojdm iyde rlrx'
#         EMAIL_USE_TLS = True


# Step 18:- App (views.py)
#           # 📌 SEND TEST EMAIL
#         def send_test_email(request):
#                 subject = 'Test Email'
#                 message = 'This is a test email sent from Django.'
#                 from_email = 'youremail@gmail.com'
#                       recipient_list = ['geuvizegebre-9696@yopmail.com']  # Replace with actual recipient email


#                 try:
#                          send_mail(subject, message, from_email, recipient_list)
#                          return render(request, 'email_sent.html', {'message': 'Test email sent successfully!'})
#                          except Exception as e:
#                             return render(request, 'email_sent.html', {'message': f'Error sending email: {str(e)}'})


# Step 19:- App(urls.py)
#         from django.urls import path
#         # from . import views
#         from .views import *


# urlpatterns = [
#     path('students/', student_list, name='student_list'),
#     path('add/', add_student, name='add_student'),
#     path('update/<int:id>/', update_student, name='update_student'),
#     path('delete/<int:id>/', delete_student, name='delete_student'),
#     path('send-test-email/', send_test_email, name='send_test_email'),
# ]


# Step 20:- Make a HTML File Which Will Be Email_Seent.html

