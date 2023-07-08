# reddit-crawler
Brandefense 2023 Internship Camp

# endpoints
admin/ <br />
users/ <br />
api-auth/login/ <br />
api-auth/ logout/ <br />
postsSoup/

# Celery Work
celery -A crawler_soup worker --loglevel=info <br />
celery -A crawler_soup beat --loglevel=info

# users
python3 manage.py createsuperuser
