#Lesson about docker


## Command download docker image from docker hub and run container in detached mode
`docker run -d -p 80:80 docker/getting-started`
* ### Container - изолированная операционная система запущенная на компьютере
* ### Image - образ будущей системы там есть все зависимости, установленны все программы и т.д. но нет файлов виртуального окружения
You'll notice a few flags being used. Here's some more info on them:

* `-d` - run the container in detached mode (in the background)
* `-p 80:80` - map port 80 of the host to port 80 in the container
* `docker/getting-started` - the image to use


##STOP/RM docker

* `docker ps` - show all running containers
* `docker ps -all` show all running and stop containers
* `docker stop [container id]` stop container
* `docker rm [container id]` rm container


##Ubuntu
###Команда создаёт файл с рандомным числом
* `docker run -d ubuntu bash -c "shuf -i 1-10000 -n 1 -o /data.txt && tail -f /dev/null"`
* `docker exec [container id] cat data.txt`

###Выводи список файлов внутри контейнера
* `docker run ubuntu -it ls \`
* `docker images`
* `docker run `


##Docker build
Тут пишем питоновский файл
* `docker build -t example-image:top .`
* `docker run --name example-app example-image:top`
* `--rm` для автоуаления


##После закрытия и удаления докер контейнера вся информация из него удаляется

#Volumes
##Нужны для того, чтобы сохранять данные и не удалять их после завершения работы контейнера
* `docker volume create db`
* `docker build -t example-volume-image:top .`
* `docker run --rm --name example-volume-app -v db:/etc/todos example-volume-image:top`


