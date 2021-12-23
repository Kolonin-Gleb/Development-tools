FROM python:3.9

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/


COPY . /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

# Сообщаем, что будем использовать порт 8080
EXPOSE 8080

# Установка переменной окружения # Чтобы время в контейнере было таким же, как у пользователя
ENV TZ Europe/Moscow
# Переменные окружения можно задавать прямо при сборке контейнера, чтобы не пересобирать образ каждый раз
# # docker run --rm --name web_hello_world_container -p 8080:8080 -e TZ=Europe/Moscow web_hello_world_image
# -e TZ=Europe/Moscow = установка переменной окружения

CMD ["python3", "-u", "app.py"]

# # docker build -t web_hello_world_image .
# # docker run --rm --name web_hello_world_container web_hello_world_image

# Приложение не заработает, т.к. Docker контейнер полностью изолирован от окружения.
# Ему нужно дать команды, какие порты слушать.

# # docker build -t web_hello_world_image .
# # docker run --rm --name web_hello_world_container -p 8080:8080 web_hello_world_image
# -p 8080:8080 = на машине, где будет запущен контейнер порт 8080 будет соединен с портом 8080 самого контейнера
# Терминал формирует неверную ссылку к локальному серверу. 
# Приложение будет работать по адресу: http://localhost:8080/


# Docker volume - дисковые хранилища. Не очищаются после работы докера. Подходят для хранения БД
# docker volume ls - список активных дисковых хранилищ
# docker volume create `name` - создание
# # docker volume create web_hello_world_volume

# Команда для сборки контейнера с подключением volume, который будет хранить данные
# # docker run --rm --name web_hello_world_container -p 8080:8080 -v web_hello_world_volume:/usr/src/app/resourses web_hello_world_image
# -v имя_volume:абсолютный_путь_внутри_каталога_откуда_сохранять_данные
# /usr/src/app/resourses - папка с JSON файлом, где будут храниться данные. Они останутся после остановки контейнера
# 

