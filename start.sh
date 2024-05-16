sudo apt-get update
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
pip install -r requirements.txt
uwsgi --stop /var/www/script/uwsgi.pid
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput

uwsgi --ini uwsgi.ini
