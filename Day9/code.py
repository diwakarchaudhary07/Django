# ✅ Day  9 :- CRUD Operation.

# ## get method :-                             
# => it is used to show/fetch data from database. 
# => it is less secure , because it is visible to anyone. 


# ## post method :-
# => it is used to store or send data in database .


# What is a form ?
# => by using any form we take input data from any user and stores/send in database. 
# => 
# => in any form POST method is used.


# ## EDIT => Update  , PUT method 

# , Suppose there is a form , in which Name : Tridev  
# and we edit it , Name : Vicky 

# and click on Update Button =>   

#             POST    GET               PUT   DELETE
# ## CRUD : Create , Retrieve/ Read , Update, Delete 


# ## Retrieve => we have to use GET method , to fetch or show data from database. 
# ## Create => we have to use POST method, to store data in the database . 
# ## Update => we have to use PUT method to edit or update any data in the database. 
# ## Delete => we have to use DELETE method.

# =>Main.html

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Student CRUD</title>
#     <!-- Bootstrap CDN -->
#     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
# </head>
# <body class="bg-light">
# <div class="container mt-5">
#     <div class="text-center mb-4">
#         <h1 class="text-primary">Student CRUD Operation</h1>
#         <p class="text-muted">Django CRUD Project</p>
#         <p>HELLO Tridev</p>
#     </div>

#     {% block content %}
#     <!-- Content will be inserted here -->
#     {% endblock %}

#     <div class="text-center mt-4">
#         <p class="text-secondary">&copy; 2026 Student CRUD. All rights reserved.</p>
#     </div>
# </div>
# <!-- Bootstrap JS -->
# <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
# </body>
# </html>


# File:- OTHER.html

# We have to Keep only common code in Main.html
# and 
# we have to use this main.html in another html file.
# Just Like This :- 

# {% extends 'main.html' %}
# {% block content %} 
# <div class="card shadow p-4">
#     <div class="d-flex justify-content-between mb-3">
#         <h3>Student List</h3>
#         <a href="/add/" class="btn btn-success">+ Add Student</a>
#     </div>
# </div>
# {% endblock %}
# ✅ Benefits of main.html File
# 1. Reusable Common Layout
# main.html contains common parts of website pages like:
# Header
# Navbar
# Footer
# Sidebar
# CSS / JS links
# Instead of writing these again and again in every page, you keep them in one file.
# 2. Saves Time
# You write code once in main.html and use it on multiple pages.
# Example:
# Home page
# About page
# Contact page
# All can use the same layout.
# 3. Easy Maintenance
# If you want to change navbar or footer:
# ✅ Change only in main.html
# ✅ Simple Meaning
# main.html = Master page / Base template / Parent layout
# Other pages inherit it.
# ✅ Real-Life Example
# Think of main.html like a house design template.
# Every room has same:
# Doors
# Windows
# Roof
# Only room content changes.
# ✅ Final Answer
# main.html file is useful because it helps create a common website layout, saves coding time, makes maintenance easier, and keeps code clean using template inheritance.

