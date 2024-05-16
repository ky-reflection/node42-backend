uwsgi --stop /var/www/script/uwsgi.pid
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput
uwsgi --ini uwsgi.ini
