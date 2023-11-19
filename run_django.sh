python3 -m venv myvenvironment
source myvenvironment/bin/activate
python3 -m pip install Django
pip install django-allauth
deactivate
python3 manage.py createsuperuser
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
