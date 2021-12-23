# Lesson about docker 2

## Write sample flask web-site
### Folder: `/web_site`
* `docker build -t web-site-image:top .`
* `docker run --rm --name web-site-cont -p 8080:80 web-site-image:top`
#### Launch: `http://localhost:8080`


## Write sample flask web-site-with-logs
### Folder: `/web_site_logs`
* `docker build -t web_site_logs_image:top .`
* `docker volume create web_site_logs`
* `docker run --rm --name web_site_logs_cont -p 8000:80 -v web_site_logs:/etc/db web_site_logs_image:top`


## Write sample flask web-site-with-env
### Folder: `/web_site_env`
* `docker build -t web_site_env_image:top .`
* `docker volume create web_site_env`
* `docker run --rm --name web_site_env_cont -p 8000:80 -v web_env_logs:/etc/db -e HOST=0.0.0.0 -e PORT=80 web_site_logs_image:top`

## Network
### Folder: `/network`
* `docker network create --subnet 172.20.0.0/16 net_db`
* `docker run --name postgres -e POSTGRES_PASSWORD=password -e POSTGRES_USER=postgres -e POSTGRES_DB=postgres -d postgres:10-alpine`
* `docker network connect --ip 172.20.0.5 net_db postgres`
* `docker build -t network_image:top .`
* `docker run --name network_cont -p 8000:80 --rm --network net_db -e HOST=0.0.0.0 -e PORT=80 network_image:top`

# Compose
### Folder: `/compose`