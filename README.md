# my_project_6 (Store)

## Пет проект - магазин компьютерных комплектующих, на базе Django 2.2 ORM + DRF
Взаимодействие с данными возможно через:
- Django стандартную админ панель.
- Веб интерфейс.
- API интерфейс.

## Стек
- Python 3.9
- Django 2.2
- Django REST framework 3.13
- Drf_yasg 1.2 (ReDoc + Swagger) API documentation

## Развертование проекта:
```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser (Для "не безопасных" операций с базой нужны права.)
python manage.py loaddata fixtures.json (загрузка тестовый данных в базу)
```
```sh
Или Docker:
pip instal docker
docker build -t store .   (команда из папки с файлом DOckerfile) 
docker run --name store -it -p 8000:8000 store
docker exec store python manage.py makemigrations
docker exec store python manage.py migrate
docker exec store python manage.py createsuperuser (Для "не безопасных" операций с базой нужны права.)
docker exec store python manage.py loaddata fixtures.json (загрузка тестовый данных в базу)
```
## Работа с базой через веб интерфейс:
- View реализованы через функции с целью отработки навыков, оптимальее было бы через ViewSet.
- Взаимодействие с моделью User частично изменено, доступно через веб интерфейс.
- Веб администрирование доступно через staff_panel, ограничено пермишенами.
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
"*" - ограничены пермишенами, - только для зарегестрированных пользователей с соответствующими правами.

## Работа с базой через API интерфейс:
- API построен на базе ViewSet, с доработкой.
- Кастомные запросы на APIView
- Взаимодействие с API так же ограничено пермишенами(для "не безопасных" запросов).
- Для аутентификацию используем стандартный модуль DRF - Authtoken
- Для тестирования использовал REST Client for Visual Studio Code, см. файл requests.http в папке с проектом. 
```sh
http://127.0.0.1:8000/api-token-auth/ - получение токена по логину/паролю(например superuser)
http://127.0.0.1:8000/swagger/ - Swagger документация
http://127.0.0.1:8000/redoc/ - ReDoc документация
```