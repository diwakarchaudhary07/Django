# ✅ Day 1 – Django 

# Q1- What is Django? Why do we need to use this?
# Django is a high-level Python web framework used to build websites and web applications quickly and efficiently. It follows the MVT (Model-View-Template) architecture and comes with many built-in features.
# 👉 In simple words:
#  Django helps developers create powerful websites without writing everything from scratch.

# 🔥 Why do we use Django?
# Here are the main reasons:
# 1. ⚡ Fast Development
# Django provides ready-made components (like admin panel, authentication).
# You can build projects much faster compared to starting from zero.
# 2. 🔒 Security
# Protects against common attacks like:
# SQL Injection
# Cross-Site Scripting (XSS)
# CSRF attacks
# Built-in security features make apps safer.
# 3. 🧩 Built-in Features
# Admin panel (no need to build manually)
# User authentication system
# ORM (database handling without SQL)
# 4. 📈 Scalable
# Used by large platforms like:
# Instagram
# Pinterest
# Can handle both small and large projects.
# 5. 🧼 Clean & Organized Code
# Follows DRY (Don’t Repeat Yourself) principle
# Makes code easy to maintain and reuse
# 6. 🌐 Works with Databases Easily
# Supports databases like SQLite, MySQL, PostgreSQL
# You don’t need to write complex SQL queries

# Q2- How to set up a basic project in Django?
# 1. Install Django
# First, make sure you have Python installed:-
# pip install django
# Check installation:-
# django-admin --version

# 2. Create a New Project
# django-admin startproject myproject
# 👉 This creates a folder like:
# myproject/
# ├── manage.py
# └── myproject/
#     ├── __init__.py
#     ├── settings.py
#     ├── urls.py
#     ├── asgi.py
#     └── wsgi.py



# 3. Run the Server
# First Go inside The project folder:- cd myproject
# For Running Project:- python manage.py runserver

# 👉 Open browser:
# http://127.0.0.1:8000/
# You’ll see Django’s welcome page 🎉


# 4. Create an App
# Django projects contain apps.
# python manage.py startapp myapp
# 👉 Folder created:
# myapp/
# ├── views.py
# ├── models.py
# ├── admin.py
# └── apps.py

# 5. Register the App
# Open settings.py and add:-
# INSTALLED_APPS = [
#    'myapp',
# ]

# 6. Create a View
# In views.py file:-
# from django.http import HttpResponse

# def home(request):
#    return HttpResponse("Hello, Django!")


# 7. Connect URL
# Edit urls.py file:-
# from django.contrib import admin
# from django.urls import path
# from myapp.views import home

# urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', home),
# ]

# 8. Run Again
# python manage.py runserver
# 👉 Open:
# http://127.0.0.1:8000/

# Q3- What is the admin panel?
# The Admin Panel (Django Admin) is a built-in dashboard that allows you to manage your website’s data without coding.
# 👉 In simple words:
#  It is a ready-made control panel where you can add, edit, delete, and view data easily.

# 🎯 Why is Admin Panel useful?
# 1. ⚡ No need to build backend manually
# Django already gives you a fully functional admin interface
# 2. 📝 Easy Data Management
# You can manage:
# Users 👤
# Products 🛒
# Blog posts 📰
# Database records
# 3. 🔐 Secure Access
# Only authorized users (admin/staff) can login
# 4. ⏱️ Saves Development Time
# No need to create CRUD (Create, Read, Update, Delete) pages manually

# ⚙️ How to Access Admin Panel
# 1. Create Superuser
# python manage.py createsuperuser
# 2. Run Server
# python manage.py runserver
# 3. Open in Browser👉 http://127.0.0.1:8000/admin/
# Login with your credentials

# 🔧 How to Show Your Data in Admin
# In admin.py:
# from django.contrib import admin
# from .models import MyModel

# admin.site.register(MyModel)
# 👉 Now your model appears in admin panel 🎉

# Q4- How to create a project using Django Command And how to create any app in Django using command?

# Similar As Point Q2

# Q5- What  is frame work and what is a library?
# 🧠 What is a Framework?
# A framework is a pre-built structure that provides a complete foundation to develop applications.
# 👉 It controls the flow of the program and tells you how to build your project.
# 📌 Example:
# Django
# Angular
# 🎯 Key Points:
# You follow the framework’s rules
# It decides how your code runs
# Provides ready-made tools & structure
# 👉 This is called Inversion of Control (framework calls your code)

# 📚 What is a Library?
# A library is a collection of pre-written functions or tools that you can use when needed.
# 👉 You are in control — you decide when and where to use it
# 📌 Example:
# NumPy
# jQuery
# 🎯 Key Points:
# You call the library
# No strict structure
# Used to perform specific tasks

# ⚖️ Difference Between Framework & Library
# Feature
# Framework 🏗️
# Library 📚
# Control
# Framework controls flow
# You control flow
# Usage
# Full structure
# Specific functions
# Flexibility
# Less flexible
# More flexible
# Example
# Django
# NumPy


# 🎯 Simple Example
# Using a Framework = Like building a house with a fixed blueprint 🏠
# Using a Library = Like using tools (hammer, drill) when needed 🔧

# 🧾 Final Short Answer (Exam Ready)
# Framework: A pre-defined structure that controls application flow.
# Library: A collection of functions used by the developer when needed.



# Main Start:- How TO Make A Basic Django Project
# ⚙️ 1. Install Django
# First, make sure you have Python installed:-
# pip install django
# Check installation:-
# django-admin --version

# 📁 2. Create a New Project
# django-admin startproject myproject
# 👉 This creates a folder like:
# myproject/
# ├── manage.py
# └── myproject/
#     ├── __init__.py
#     ├── settings.py
#     ├── urls.py
#     ├── asgi.py
#     └── wsgi.py



# ▶️ 3. Run the Server
# First Go inside The project folder:- cd myproject
# For Running Project:- python manage.py runserver

# 👉 Open browser:
# http://127.0.0.1:8000/
# You’ll see Django’s welcome page 🎉

