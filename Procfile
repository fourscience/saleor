release: python manage.py migrate --no-input
web: gunicorn --bind :$PORT --workers 2 --worker-class uvicorn.workers.UvicornWorker saleor.asgi:application
celeryworker: celery -A saleor --app=saleor.celeryconf:app worker --max-memory-per-child=12000 --without-heartbeat --without-gossip --without-mingle --loglevel=info -E
