New virtual environment -- virtualenv env

Activate the virtualenvironment -- source env/bin/activate

Installing django 
`pip install django`

Installing pillow -- pip install pillow

Installing boostrap3-datetime -- pip install bootstrap3-datetime

Installing crispy-forms -- pip install django-crispy-forms

Make users migrations -- python manage.py makemigrations users

Make logistics migrations -- python manage.py makemigrations logistics

General migrations -- python manage.py makemigrations

Migrate -- python manage.py Migrate

Creating superuser -- python manage.py createsuperuser

Opening the shell -- python manage.py shell

Associate profile with user -- 

    -- from django.contrib.auth.models import User
    
    -- user = User.objects.first()
    
    -- from users.models import Profile
    
    -- Profile.objects.create(user=user, image='default.png')
    
    -- exit()
    
    
Run App -- python manage.py runserver

--

