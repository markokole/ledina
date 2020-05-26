# Pilot za vpis kandidatov za sprejem na srednjo solo

Postgres baza za shranjevanje podatkov
Django za spletno stran in manipulacijo s podatki

```bash
docker build . --tag=markokole/ledina
```

```bash
docker push markokole/ledina:latest
```

## Docker Compose

```bash
docker-compose up -d
```

```bash
docker exec -it ledina_ledina_1 /bin/sh
```

## Docker

```bash
docker run -itd --rm -v C:\marko\GitHub\ledina\project:/project -p 8000:8000 --name ledina markokole/ledina
```

```bash
docker exec -it ledina /bin/sh
```

## Inside container

### Start server

```bash
python3 manage.py runserver 0.0.0.0:8000
```

### Enter Ipython

```bash
python3 manage.py shell -i ipython
```
