# Dependent Dropdown Example

[![Python Version](https://img.shields.io/badge/python-3.8-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.2-brightgreen.svg)](https://djangoproject.com)

Example code about how to implement dependent dropdown lists with Django.

![Dependent Dropdown Example Screenshot](https://simpleisbetterthancomplex.com/media/2018/01/dependent-dropdown-3.png)

Read the blog post [How to Implement Dependent/Chained Dropdown List with Django](https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html).

This project is deployed at [dependent-dropdown-example.herokuapp.com](http://dependent-dropdown-example.herokuapp.com/hr/add/).

## How to Start 🏠

Clone this project and open the folder.

```bash
git clone https://github.com/ba1x/django-dependent-dropdown.git
cd django-dependent-dropdown
```

Create and enter the [Python environment](#python-environment).

```bash
python3 -m venv env     # create the python environment
. env/bin/activate      # enter to the environment
```

Install the requirements:
```
pip install -r requirements.txt
```

**Migrate** the database and **run** the webserver on **PORT 3001**.

```bash
./manage.py migrate         # start the project 
./manage.py runserver 3001  # run the webserver
```

## License

The source code is released under the [MIT License](https://github.com/sibtc/dependent-dropdown-example/blob/master/LICENSE).

## Credits

This work is forked from [here](https://github.com/sibtc/dependent-dropdown-example).