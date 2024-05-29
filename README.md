# Portal de Proveedores

Portal para atender solicitudes de compra. 
Con diferentes roles para registrar solicitudes y aprobarlas.

## Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com:JEnriquePS/portal_providers.git
    $ cd portal_providers

Activate the virtualenv for your project and install project dependencies:

    $ pip install -r requirements/dev.txt 

Then simply apply the migrations:

    $ python manage.py makemigrations
    $ python manage.py migrate

You can now run the development server:

    $ python manage.py runserver --settings=PortalProviders.settings.dev

## Authors
JEnriquePS - https://github.com/JEnriquePS