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
$ docker network create project_network
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

# First instance
python manage.py runserver 0.0.0.0:8000

# Second instance
python manage.py runserver 0.0.0.0:8001

# Third instance
python manage.py runserver 0.0.0.0:8002
