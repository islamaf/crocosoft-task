FROM python:3.9.6-slim-buster

RUN apt-get update
RUN apt-get install default-libmysqlclient-dev libmariadb-dev gcc -y

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 5000

CMD ["flask", "--app", "car_rental:create_app('dev')", "run", "-h", "0.0.0.0", "-p", "5000"]