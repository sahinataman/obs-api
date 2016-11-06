Installation

virtualenv venv

venv\Scripts\active

pip install -r req.txt

django-admin.py startproject obs

git clone https://github.com/comuOBS/obs-api.git

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
