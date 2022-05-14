# Elta project

## Set up the environment

Make sure you have python3, pip and all dependencies installed on your machine.

For linux:

```bash
# clone the repository
git clone https://github.com/Alex171823/elta.git

#go to project folder
cd backend
```

# make virtual environment
python3 -m venv .env

# activate vitrual environment
source .env/bin/activate

# install dependencies.
pip install -r requirements.txt

# make migrations to database. SQLite database will be created automatically 
# in the project folder
python manage.py makemigrations
python manage.py migrate

# create superuser
python manage.py createsuperuser

# run
python manage.py runserver
```
