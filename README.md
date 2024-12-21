# unio

### For Django Running on Docker
Be sure to run the first migration and create a superuser first before
creating any apps 

### Create Docker Secrets From a file
The file was located on the root project directory and must be included in .gitignore file

```bash
$ docker swarm init # Initialize Docker Swarm
$ echo "sample_value" > ./app-secrets/secret.txt
$ docker secret ls # only for docker secrets create
$ docker secret rm my_secret # delete secret
```

# Clean Slate Images

```bash
$ docker system prune -a && docker images prune -a && docker volume prune -a
```

### Build & run container

```bash
$ docker compose up --build -d
```

### Running Migrations and Creating Superuser

```bash
$ docker-compose exec backend-api python manage.py migrate --noinput
$ docker-compose exec backend-api python manage.py createsuperuser 
```

### Generate Secret Key

```bash
$ python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```