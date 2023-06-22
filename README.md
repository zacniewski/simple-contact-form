# Simple Contact Form

### Requirements
1. Docker.

### Running the project
1. `Makefile` was created to help user with running the project.
2. To initialize the project: `make docker-up`.
3. To create the superuser: `make create-superuser` (login: `admin`, password: `admin123`).
4. To create the non-admin user: `make create-user` (login: `testuser`, password: `test1234`).
5. To check functionalities you should log in with aforementioned credentials.
6. Fixtures `contacts.json` (40 contacts) were created. To apply them:  `make load-fixtures`
7. To run project in the browser, go to the [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### Tests
1. Tests were created with [pytest-django](https://pytest-django.readthedocs.io/en/latest/) and [pytest-drf](https://pypi.org/project/pytest-drf/).
2. All test are placed in `tests` directory.
3. To run the tests: `make test-contacts`.
4. To run `coverage`: `make run-coverage` and then `make coverage-html` to generate HTML report.
5. At this moment coverage result is 89%.

### Structure of the project
```bash
.
├── contacts
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── static
│   │   ├── css
│   │   └── js
│   ├── urls.py
│   └── views.py
├── contacts.json
├── core
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── docker-compose.yml
├── Dockerfile
├── Makefile
├── manage.py
├── pytest.ini
├── README.md
├── requirements.txt
├── templates
│   ├── base.html
│   ├── contact_list.html
│   ├── create_contact.html
│   ├── delete_contact.html
│   ├── home_page.html
│   ├── _pagination.html
│   ├── registration
│   │   ├── logged_out.html
│   │   └── login.html
│   └── update_contact.html
└── tests
    ├── conftest.py
    └── test_contacts.py

```