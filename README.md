SETUP

First make sure you have Python 2.7 installed, that's what this will use.

You should also get and install the postgres app for Mac (assuming you're on mac) - https://postgresapp.com/

1. Create a folder called access_hack_repository (or whatever). Navigate to it and clone the git repo into it. 

2. Create new virtual environment. This should live inside the 

cd access_hack
virtualenv venv --python=python2.7

3. Launch the new environment:

source venv/bin/activate

4. Install all requirements listed in the requirements.txt file. This will install django and some other dependencies.

pip install -r ../requirements.txt

5. Create the database

psql
(enters postgres)

CREATE DATABASE access_hack;
CREATE USER access_user WITH PASSWORD 'floweryacht7890&*()';
GRANT ALL PRIVILEGES ON DATABASE access_hack TO access_user;

\q (to quit)

6. Run all the pending database migrations

./manage.py migrate

7. Launch the server

./manage.py runserver


