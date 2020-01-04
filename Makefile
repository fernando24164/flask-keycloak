.PHONY:run

install:
	virtualenv ~/.virtualenv/flask-keycloak
	source ~/.virtualenv/flask-keycloak/bin/activate && pip install -r requirements.txt

run:
	gunicorn wsgi:app -w 1
	docker-compose up -d
