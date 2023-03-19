define USAGE

Commands:
init      Install Python dependencies with pipenv
test      Run linters, test db migrations and tests.
serve     Run app in dev environment.
endef
export USAGE
help:
@echo "$$USAGE"

init:
pip3 install pipenv
pipenv install --dev --skip-lock
pip install flask==2.0.0
pip install Werkzeug~=2.0.0
pip install jinja2~=3.0.3
pip install Flask-SQLAlchemy==2.4.4
serve:
FLASK_APP=app.py pipenv run flask run
