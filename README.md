                              JOB PORTAL
                              
                              
Technology Stack

python

Django

Chat Creation

    - create app chat

    - add app into installed apps

    - create template

    - create view

    - create urls

    - Integrate Channels
        * add in job_portal_project.asgi file
        * add the Daphne library to the list of installed apps
            pip install daphne
            pip install channels
        * edit the job_portal_project.settings.py 

        * create and edit chat/consumer.py file
        * create and edit chat/routing.py file

        * edit job_portal_project.asgi file to get chat.routing module
        * run migrations to apply database changes

        * pip install channels_redis
        * configure channels in settings.py file


