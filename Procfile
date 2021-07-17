release: python corona_api/manage.py migrate
release: python data_fetch/fetch.py
web: gunicorn --pythonpath corona_api corona_api.wsgi

