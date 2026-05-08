# ✅ Day  5 – Connecting PGSQL 

# How To Connect Pgsql In Django:-

# Step 1:- Run This Command In The Terminal pip install psycopg2 

# Step 2 :- We have to edit DATA base connectivity PART in settings.py

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'your_db_name',
#         'USER': 'postgres',
#         'PASSWORD': 'your_password', 
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# Step 3 :- Creating Data Base IN PGSQL With Same Name

# Step 4 :- Running Two Command 
#                python manage.py makemigrations
#                python manage.py migrate
#  Run the Server
