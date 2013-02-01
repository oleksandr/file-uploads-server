file-uploads-server
===================

A buildout/nginx based project layout that creates a web server to handle uploaded files (using nginx uploads module) and to pass the request further to a pre-configured backend.
This template can be used as a good starting point for the web-application that handles file uploads to avoid passing the uploads through the proxy (load-balancer).

The template relies on:
* Buildout
* Nginx
* Supervisord
* gunicorn
* Flask

The main configuration resides in buildout.cfg file. The template includes an example backend in src/ folder.

Installation
-------------
Typical buildout procedure:

    $ python bootstrap.py
    $ bin/buildout

After the last command you will receive a directory structure that looks like:

    $ ls -1
    README.md
    bin
    bootstrap.py
    buildout.cfg
    develop-eggs
    downloads
    eggs
    etc
    parts
    src
    templates
    var

Start the services:

    $ bin/supervisord

Query the status for services:

    $ bin/supervisorctl status
    Backend-Memmon                   RUNNING    pid 98675, uptime 0:33:28
    Nginx-Memmon                     RUNNING    pid 98674, uptime 0:33:28
    backend                          RUNNING    pid 98677, uptime 0:33:28
    nginx                            RUNNING    pid 98676, uptime 0:33:28

Once all the services are up and running open in your browser the following url: [http://localhost:8080](http://localhost:8080/ "http://localhost:8080")



