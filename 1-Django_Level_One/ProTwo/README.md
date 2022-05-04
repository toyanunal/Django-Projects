## **Django Level 1**

### creating a django project & application

- official and perfect tutorial: https://docs.djangoproject.com/en/4.0/intro/tutorial01/
- Anaconda or Atom Prompt > `conda info --envs`   ⇒ list all environments
Anaconda or Atom Prompt > `conda create --name djangoenv django`   ⇒ create a django environment
Anaconda or Atom Prompt > `conda activate djangoenv`   ⇒ activate django environment
- Atom Prompt > `django-admin startproject first_project`   ⇒ create a django project
- __init__.py   ⇒ indicator that this is a python code
- settings.py   ⇒ store settings of our web app
- urls.py   ⇒ store different pages of our web app
- wsgi.py   ⇒ deploy our web app to production
- manage.py   ⇒ associate commands of our web app
- Atom Prompt > `python manage.py runserver`   ⇒ run a server on local
- Atom Prompt > `python manage.py startapp first_app`   ⇒ create a django application
Atom > first_project > settings.py > add `INSTALLED_APPS = [ 'first_app', ]`   ⇒ add newly created application to the project settings
- __init__.py   ⇒ indicator that this is a python code
- admin.py   ⇒ admin interface
- apps.py   ⇒ configuration area
- models.py   ⇒ data models area
- tests.py   ⇒ test functions area
- views.py   ⇒ handle request and return responses
- migrations folder   ⇒ store database specific information
- Atom > first_app > views.py > add `from django.http import HttpResponse`
                                                         `def index(request):`
                                                              `return HttpResponse('Hello World')`   ⇒ create a view
Atom > first_project > urls.py >add `from first_app import views`
                                                          `urlpatterns = [ path('', views.index, name='index'), ]`   ⇒ map the newly created view to urls.py file
- Applications can have their own urls.py file. But, we should call them from the project’s urls.py file.
Atom > first_app > right click > new file > `first_project\first_app\urls.py` > enter   ⇒ create a urls.py file inside the app
Atom > first_app > urls.py > add `from django.urls import path` 
                                                      `from first_app import views` 
                                                      `urlpatterns = [ path('', views.index, name='index'), ]`   ⇒ map the newly created view to application’s urls.py file
Atom > first_project > urls.py > add `from django.urls import include`
                                                           `urlpatterns = [ path('first_app/', include(first_app.urls), ]`   ⇒ map the newly created view to project’s urls.py file

### template tagging

- Templates can connect with models so that we can display data (taken straight from our database) dynamically. 
**Templates** contain the **static** parts of an html page.
**Template tags** allows us to inject **dynamic** content that our application’s views file produce.
Atom > TOP first_project > right click > new folder > `first_project\templates` > enter   ⇒ create a templates folder inside the top first_project folder
Atom > first_project > settings.py > add `import os` 
                                                                  `TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')`   ⇒ define extension templates folder based on base project directory
                                                                  `TEMPLATES = [ { 'DIRS': [TEMPLATE_DIR, ], }, ]`   ⇒ map new templates to project’s settings.py file
Atom > templates > right click > new file > `first_project\templates\first_app\index.html` > enter   ⇒ create an html file
Atom > templates > index.html > `html` > tab or enter > inside `<body> </body>` add `{{ insert_me }}`   ⇒ add html code inside the index.html file; **{{ insert_me }}** is the **template tag for simple text injections**
Atom > first_project > views.py > add `from django.shortcuts import render`
                                                              `def index(request):`
                                                                  `my_dict = {'insert_me' : 'Hello I am from views.py!'}`
                                                                  `return render(request, 'first_app/index.html', context=my_dict)`   ⇒ create a view
- Atom > TOP first_project > right click > new folder > `first_project\static\images` > enter   ⇒ create a static/images folder inside the top first_project folder (also add a .jpg file inside the folder)
Atom > first_project > settings.py > add `import os` 
                                                                  `STATIC_DIR = os.path.join(BASE_DIR, 'static')`   ⇒ define extension of static folder based on base project directory
                                                                  `STATIC_URL = '/static/'`
                                                                  `STATICFILES_DIRS = [ STATIC_DIR, ]`   ⇒ map new static files to project’s settings.py file
Atom > templates > right click > new file > `first_project\templates\first_app\index.html` > enter   ⇒ create an html file
Atom > templates > index.html > `html` > tab or enter > under `<!DOCTYPE html>` add `{% load static %}` > inside `<body> </body>` add `<img src="{% static 'images/Gokc.jpg' %}" alt="Alternatif text"/>`   ⇒ add html code inside the index.html file; **{% load static %}** is the **template tag for complex injections**
