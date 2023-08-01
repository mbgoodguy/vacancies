# Vacancies

Run database (docker)

```
docker run --name amazing_hunting_postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
```
If get  ```Error starting userland proxy: listen tcp4 0.0.0.0:5432: bind: address already in use``` just follow this steps:
1. ```sudo service postgresql stop```
2. ```docker start amazing_hunting_postgres```


# Default PostgreSQL settings:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
