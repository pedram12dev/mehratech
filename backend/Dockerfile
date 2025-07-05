FROM python:3.10-slim

WORKDIR /code/backend/


COPY requirements.txt /code/backend/

RUN apt-get update && apt-get install -y gcc libpq-dev curl build-essential python3-dev && apt-get clean

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . /code/backend/

EXPOSE 8000

CMD ["watchmedo", "auto-restart", "--directory=.", "--pattern=*.py", "--recursive", "--", "gunicorn", "mehratech.wsgi:application", "--bind", "0.0.0.0:8000"]