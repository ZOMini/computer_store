# my_project_6 (Store)
## Пет проект - магазин компьютерных комплектующих, на базе Django 2.2 ORM + DRF
Взаимодействие с данными возможно через:
- Django стандартную админ панель.
- Веб интерфейс.
- API интерфейс.

## Развертование проекта:
```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser(Для "не безопасных" операций с базой нужны права.)
python manage.py loaddata fixtures.json (загрузка тестовый данных в базу)
```
## Работа с базой через веб интерфейс:
- Взаимодействие с моделью User частично изменено, доступно через веб интерфейс.
```sh
http://127.0.0.1:8000/ - index стартовая страница
http://127.0.0.1:8000/store/item/<int:item_id>/  
http://127.0.0.1:8000/item/<int:item_id>/edit/ *
http://127.0.0.1:8000/item/order/<int:name_id>/  
http://127.0.0.1:8000/create_item/ *
http://127.0.0.1:8000/name/<int:name_id>/ 
http://127.0.0.1:8000/name/<int:name_id>/edit/ *
http://127.0.0.1:8000/create_name/  *
http://127.0.0.1:8000/category/<int:category_id>/
http://127.0.0.1:8000/category/<int:category_id>/edit/  *
http://127.0.0.1:8000/create_category/  *
http://127.0.0.1:8000/all_categories/
http://127.0.0.1:8000/staff_panel/  *
```
"*" - ограничены пермишенами, - только для зарегестрированных пользователей с соответствующими провами.

## Работа с базой через API интерфейс:
- 
```sh
http://127.0.0.1:8000/api-token-auth/ - получение токена по логину/паролю(например superuser'a))
http://127.0.0.1:8000/swagger/
http://127.0.0.1:8000/redoc/
```