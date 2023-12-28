![](https://raw.githubusercontent.com/saasitive/docker-compose-django-celery-redis-postgres/main/media/banner.jpg)

# Docker Compose for Django, Celery, Redis, and Postgres

Article with implemenation details: [Docker compose with Django 4, Celery, Redis and Postgres](https://saasitive.com/tutorial/django-celery-redis-postgres-docker-compose/)

#### Build docker

```
sudo docker-compose build
```

#### Start docker

```
docker-compose -f docker-compose-develop.yml up -d
sudo docker-compose up
```

#### Build and run in detached mode

```
sudo docker-compose up --build -d
```

### Stop docker-compose

```
sudo docker-compose down
```

# Others:
===========
```
docker stop proj_celery-worker proj_celery-redis proj_celery-db proj_celery-server
docker rm -v proj_celery-worker proj_celery-redis proj_celery-db proj_celery-server
docker image rm docker-compose-django-celery-redis-postgres_server docker-compose-django-celery-redis-postgres_worker
```

## Desplegar el develop

```
cd /home/wilson/CODE/proy_celery/docker-compose-django-celery-redis-postgres
docker-compose -f docker-compose-develop.yml up -d
```

## Revisar los logs
```
docker logs --tail 100 proj_celery-server
docker exec -ti proj_celery-server bash
```

# References:
- https://github.com/realpython/dockerizing-django/blob/master/docker-compose.yml
- https://realpython.com/django-development-with-docker-compose-and-machine/
- https://github.com/albertorc87/redisxdjango/blob/main/README.md
- https://londonappdeveloper.com/deploying-django-with-docker-compose/
- https://www.cloudbees.com/blog/using-docker-compose-for-python-development
