FROM python:3.10-slim

WORKDIR /code/backend/


COPY requirements.txt /code/backend/

RUN apt-get update 

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . /code/backend/

EXPOSE 8000

CMD ["gunicorn","mehratech.wsgi", ":8000"]