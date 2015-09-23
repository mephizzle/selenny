.PHONY: requirements install


bin/pip:
	virtualenv .

requirements: bin/pip
	bin/pip install -r requirements.txt

install: requirements
	bin/python manage.py syncdb --noinput
	bin/python manage.py migrate

run:
	bin/python manage.py runserver

clean:
	-@rm -rf bin lib local include db.sqlite3
