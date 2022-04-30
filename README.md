# my_project_6 (Store)
## Пет проект магазина, на базе Django 2.2 + DRF
Взаимодействие с данными возможно через:
- Django стандартную админ панель.
- Веб интерфейс.
- API интерфейс.

## Развертование проекта
```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

