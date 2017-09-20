# mf-dataentry
Django app that provides a single data entry point and exports its data to 

## Installation

```
sudo apt-get install freetds-dev
pew new mf_dataentry
# for more info about pymssql check ffapb/ffa-blotter requirement.txt
pip install django progressbar33 git+https://github.com/pymssql/pymssql.git
```

# Import marketflow

- copy importMarketflow.sh.dist to importMarketflow.sh and set env vars for database connection
- `./importMarketflow.sh --debug`

