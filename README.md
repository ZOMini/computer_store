# Сomputer store

## Пет проект - магазин компьютерных комплектующих, на базе Django 4.0.4 ORM + DRF
Взаимодействие с данными возможно через:
- Django стандартную админ панель.
- Веб интерфейс.
- API интерфейс.


## Стек
- Python 3.9
- Django 4.0.4
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
python manage.py loaddata fixtures.json (загрузка тестовый данных в базу.)
```
```sh
Или Docker:
https://docs.docker.com/engine/install/ - Установка Docker.
docker build -t store .   (команда из папки с файлом DOckerfile.) 
docker run --name store -it -p 8000:8000 store
docker exec store python manage.py makemigrations
docker exec store python manage.py migrate
docker exec store python manage.py createsuperuser (Для "не безопасных" операций с базой нужны права.)
docker exec store python manage.py loaddata fixtures.json (Загрузка тестовый данных в базу.)
```
```sh
Деплой на удаленный сервер(проверял на Ubuntu 20.04):
Подготавливаем сервер:
sudo systemctl stop nginx
sudo apt update
sudo apt install docker.io
sudo apt install curl
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
Готовим репозитарий:
В 'Actions secrets' в настройках вашего проекта на GitHub внесите необходимые параметры сервера:
HOST - Публичный ip адрес сервера
USER - Пользователь сервера
PASSPHRASE - Если ssh-ключ защищен фразой-паролем
SSH_KEY - Приватный ssh-ключ
После успешного коммита и прохождения тестов ваш проект автоматически будет настроен на сервере.
sudo docker-compose exec web python manage.py createsuperuser - создаем суперпользователя
sudo docker-compose exec web python manage.py loaddata fixtures.json - Загрузка тестовый данных в базу.
```
## Работа с базой через веб интерфейс:
- Взаимодействие с моделью User частично изменено, доступно через веб интерфейс.
- Веб администрирование доступно через staff_panel, ограничено пермишенами.
- Либо стандартная Django админка. 
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
http://127.0.0.1:8000/admin/ * - стандартная django админка
```
"*" - ограничены пермишенами, - только для зарегестрированных пользователей с соответствующими правами.

## Работа с базой через API интерфейс:
- API построен на базе ViewSet, с доработкой.
- Кастомные запросы на APIView
- Взаимодействие с API так же ограничено пермишенами(для "не безопасных" запросов).
- Для аутентификацию используем стандартный модуль DRF - Authtoken
- Для тестирования использовал REST Client for Visual Studio Code, см. файл requests.http в папке с проектом. 
```sh
http://127.0.0.1:8000/api-token-auth/ - получение токена по логину/паролю(например superuser).
http://127.0.0.1:8000/api/swagger/ - Swagger документация.
http://127.0.0.1:8000/api/redoc/ - ReDoc документация.
``` 