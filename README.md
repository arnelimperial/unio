# unio

#### For Django Running on Docker
Be sure to run the first migration and create a superuser first before
creating any apps 

#### Create Docker Secrets From a file
The file was located on the root project directory and must be included in .gitignore file

```bash
$ docker swarm init # Initialize Docker Swarm
$ echo "sample_value" > ./app-secrets/secret.txt
$ docker secret ls # only for docker secrets create
$ docker secret rm my_secret # delete secret
```

#### Create Docker Network

```bash
$ docker network create app-network
$ docker network ls
```

#### Clean Slate

```bash
$ docker system prune -a && docker images prune -a && docker volume prune -a
```

#### Build & run container

```bash
$ docker compose up --build -d
```

#### Running Migrations, Creating Superuser & Generate Django App

```bash
$ docker-compose exec backend-api python manage.py migrate --noinput
$ docker-compose exec backend-api python manage.py createsuperuser
$ docker-compose exec backend-api python manage.py startapp users 
```

#### Generate Secret Key

```bash
$ python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

#### Checking Directories inside a Running Containers

```bash
$ docker-compose up -d # run the service; can be on detach mode
$ docker-compose exec backend-api ls /usr/src/app # service name & the volume
$ docker-compose exec backend-api ls -la /usr/src/app # check hidden files
$ docker-compose exec backend-api sh # interact with the backend-api service environment
$ exit 
```

#### Generate a Self-Signed SSL Certificate with OpenSSL (Django)

```bash
$ mkdir ssl && openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
-out ./ssl/cert.pem -keyout ./ssl/key.pem \
-subj "/C=US/ST=State/L=City/O=Organization/OU=Unit/CN=localhost"
# Run Django localhost HTTPS
$ python manage.py runsslserver 8000 --certificate ../ssl/cert.pem --key ../ssl/key.pem
```



