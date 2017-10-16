# mf-dataentry
Django app that provides a single data entry point and exports its data to 

## Installation

```
sudo apt-get install freetds-dev
pew new mf_dataentry
# for more info about pymssql check ffapb/ffa-blotter requirement.txt
pip install django progressbar33 git+https://github.com/pymssql/pymssql.git
pip install pip PyYAML
+pip install Flask-SQLAlchemy

```

# Import marketflow

- copy importMarketflow.sh.dist to importMarketflow.sh and set env vars for database connection
- copy "app/credentials.yml.dist" to "app/credentials.yml" and set variables
- `./importMarketflow.sh --debug`

# ORM

The file `app/management/command/titre.py` is the sqlalchemy ORM file
exported from the marketflow database using [sqlacodegen](https://pypi.python.org/pypi/sqlacodegen) as such:

    > sqlacodegen --tables TITRE --outfile titre.py mssql+pymssql://user:pass@ip:port/db

# Testing

    ./manage.py test app.tests
