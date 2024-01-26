# Installation
Open your project's dertory.\
In the terminal, run the commands:
```
git init
```
```
git pull https://github.com/D0D0KU/simple_registration_with_fastapi_users.git main
```
# Сustomization
Activate the virtual environment and install the requirements:

    pip install -r requirements.txt

Then enter the following into your .env:
```
DB_NAME = your_db_name
DB_SCHEMA = your_schema_name
DB_HOST = your_db_host (default: localhost)
DB_PORT = your_db_port (default: postgresql_port=5432 or mysql_port=3306)
DB_USER = your_db_user_name
DB_PASSWORD = your_db_password

SECRET = your_secret_srting
```


