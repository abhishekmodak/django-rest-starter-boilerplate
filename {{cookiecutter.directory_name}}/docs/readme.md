### This folder will contain project-wide documentation

# {{ cookiecutter.project_name }}

{{ cookiecutter.version }}

{{ cookiecutter.description }}


# Features!

    ### Arrangements

        - Dividing settings file into base.py and dev.py/prod.py.
        - List of installed apps in a separate file and divided based on categories.
        - Configurations are in a separate file.
        - Requirements.txt is also modified in the same pattern as settings file.

    ### Modules Added

        - Designed to work with DRF, intended to reply in json and not in template.
        - Factory model from which other models will inherit.
        - Overriding delete function to make status false and store its deletion time whenever deletion is performed.
        - Custom User model making it scalable.
        - Login process
        - Logout process
        - Update password
        - Exceptions are customised so that we can add any new features on it
        - log is configured (not used in project)
        - Email setup using sendgrid (not used in project)
        - SMS integration using Twilio (not used in project)
        - Slack messaging integrated (not used in project)
        - Swagger added to find Documentation of APIs



# Procedure -

    - Install cookiecutter .
    - create project using:
            cookiecutter https://github.com/abhishekmodak/django-rest-starter-boilerplate.git
    - Enter all your data.
    - Start customizing


Author - {{ cookiecutter.author_name }}
Email - {{ cookiecutter.email }}