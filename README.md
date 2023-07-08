# reddit-crawler
Brandefense 2023 Internship Camp

# endpoints
admin/ <br />
users/ <br />
api-auth/login/ <br />
api-auth/ logout/ <br />
postsSoup/

# Celery Work
celery -A crawler_soup worker --loglevel=info
celery -A crawler_soup beat --loglevel=info
