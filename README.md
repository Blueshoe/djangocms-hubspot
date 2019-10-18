# django CMS Hubspot


A plugin for django CMS which makes integrating HubSpot easier.

It creates plugins for:

- Forms
- CTAs



## Installation


- install with `pip`:

    `$ pip install djangocms-hubspot`


- add the django app to `INSTALLED_APPS` in your settings file:
```
    INSTALLED_APPS = (
        ...
        'django_select2',
        'djangocms_hubspot',
        ...
    )
```

- run `python manage.py migrate`.


### Dependencies
- django-select2
