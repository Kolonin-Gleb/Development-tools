# Команды для этого проекта

##Docker build
* `docker build -t lesson1db-img .`
* `docker run --rm --name lesson1db-cont lesson1db-img`

##После закрытия и удаления докер контейнера вся информация из него удаляется

#Volumes
##Нужны для того, чтобы сохранять данные и не удалять их после завершения работы контейнера
* `docker volume create db-vol`
* `docker run --rm --name lesson1db-cont -v db-vol:/app/users.db lesson1db-img`





#Lesson about docker

### Container - изолированная операционная система запущенная на компьютере
### Image - образ будущей системы там есть все зависимости, установленны все программы и т.д.
### но нет файлов виртуального окружения
### Volume - дисковое хранилище, не очищающаеся после работы докера. Подходят для хранения БД

## Command download docker image from docker hub and run container in detached mode
`docker run -d -p 80:80 docker/getting-started`

You'll notice a few flags being used. Here's some more info on them:

* `-d` - run the container in detached mode (in the background)
* `-p 80:80` - map port 80 of the host to port 80 in the container
* `docker/getting-started` - the image to use

##STOP/RM docker
* `docker ps` - show all running containers
* `docker ps -all` show all running and stopped containers
* `docker stop [container id]` stop container
* `docker rm [container id]` rm container

