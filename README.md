# artwebsite
An ecommerce website for selling my artwork online and promoting my social media.

## Getting Started
Here are a list of things to understand and do in order to get this project working on your local machine.

### Core Dependencies
- [Python v3.8.9](https://www.python.org/downloads/release/python-389/)
- Django v4
- Coverage (Testing Utility)
- Pillow (Image Processing)

Python is required for this codebase.
We discovered that Python v3.8.9 is the current [stable version](https://stackoverflow.com/questions/71712258/error-could-not-build-wheels-for-backports-zoneinfo-which-is-required-to-insta)

### Create a virtual environment
`python -m venv venv`

### Activate the virtual environment
Windows:
`\venv\Scrips\activate.bin`

Mac:
`source venv/bin/activate`

### Install Requirements
`pip install -r requirements.txt`

This will read the `requirements.txt` file and use `pip` to install them.

### Database Setup
Setup the database by executing the `migrate` command:
`python manage.py migrate`
This will create a `sqlite` database and read the `store/migrations/` folder to create and populate the database with tables.

### Superuser Setup
Next, execute the following command:
`python manage.py createsuperuser`
Set username to `admin`.
Leave email blank.
Set password to `admin` and confirm. (type `y` and enter to validate a short password).

### Starting Webserver
Finally, execute the following command:
`python manage.py runserver`
This command starts a development webserver.

### Useful Links
[admin pannel](http://localhost:8000/admin) Log in using the `admin` user from above. Create some mock data to populate the database.
[local artwebsite homepage](http://localhost:8000/)