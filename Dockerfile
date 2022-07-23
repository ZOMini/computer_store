# build env
FROM python:3.9.7-slim
WORKDIR /c_store
COPY c_store/ .
RUN pip install -r requirements.txt
CMD ["gunicorn", "c_store.wsgi:application", "--bind", "0.0.0.0:8000" ]
