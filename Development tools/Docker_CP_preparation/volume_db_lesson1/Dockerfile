FROM python:3.8-slim-buster

WORKDIR /usr/src/app/

COPY requirements requirements

RUN pip3 install -r requirements

COPY . /usr/src/app/

CMD [ "python3", "-u", "volume_db.py"]
