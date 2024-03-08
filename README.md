# Alpes Real Estate - Audits

This is a real estate platform

## Deployment in local environment
### Requirements for running with docker
1. Docker
2. Docker compose

### Requirements for running with python
1. python 3.10

### Run docker
1. Modify the file name `.env.example`, should stay with the name `.env`
2. Modify the file name `alembic.ini.example`, should stay with the name `alembic.ini`
3. Modify the `.env` y `alembic.ini` file with the credentials of the environment to run
4. Create docker image and container with command `docker compose -f docker-compose-stage.yml up`
5. The project is accessible in the port http://127.0.0.1:8008

### Run python
1. Create and activate a virtual environment
2. Install dependencies with command `pip install -r requirements.txt`
3. Install pulsar cli with command `python -m pip install pulsar-client`
4. Modify the file name `.env.example`, should stay with the name `.env`
5. Modify the file name `alembic.ini.example`, should stay with the name `alembic.ini`
6. Modify the `.env` y `alembic.ini` file with the credentials of the environment to run
7. Start app with command `flask --app app/api run --host=0.0.0.0 --port 8008`
8. The project is accessible in the port http://127.0.0.1:8008


## Migrations and seeders
### Migrations
1. Run migrations with the command `alembic upgrade head`, this command will fill the database


## Eventos 
### Prepara el ambiente para probar los eventos, se debe abrir una consola para cada uno.
1. `docker-compose --profile pulsar up` 
2. `python main.py` notificador se debe entrar a app/notificaciones/
3. `python consumer_test.py` consume el evento
4. `python producer_test.py` publica el evento