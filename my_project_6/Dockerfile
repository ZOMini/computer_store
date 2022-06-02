# build env
FROM python:3.9.7-slim
WORKDIR /my_project_6
COPY . .
RUN pip install -r requirements.txt
CMD gunicorn my_project_6.wsgi:application --bind 0.0.0.0:8000
