# mf-dataentry
Django app that provides a single data entry point and exports its data to 

## Installation

```
sudo apt-get install freetds-dev
pew new mf_dataentry
# for more info about pymssql check ffapb/ffa-blotter requirement.txt
pip install django progressbar33 git+https://github.com/pymssql/pymssql.git
pip install pip PyYAML
pip install sqlalchemy

```

# Import marketflow

- copy importMarketflow.sh.dist to importMarketflow.sh and set env vars for database connection
- copy "app/credentials.yml.dist" to "app/credentials.yml" and set variables
- `./importMarketflow.sh --debug`

# ORM

The file `app/management/command/titre.py` is the sqlalchemy ORM file
exported from the marketflow database using [sqlacodegen](https://pypi.python.org/pypi/sqlacodegen) as such:
    > pip install sqlacodegen
    > pip install git+https://github.com/pymssql/pymssql.git
    > sqlacodegen --tables TITRE --outfile titre.py mssql+pymssql://user:pass@ip:port/db

# Testing

    ./manage.py test app.tests


# Docker

 - Create Dockerfile
 - Create docker-entry.sh
 - docker build . -t teamshadi/mf-dataentry:testMin
 - docker run -it -p 8008:8008 -v $PWD/db.sqlite3:/var/lib/mf_dataery/db.sqlite3 teamshadi/mf-dataentry:testMin
 
