# build env
FROM python:3.9.7-slim
WORKDIR /c_store
COPY . .
RUN pip install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0:8000"]
