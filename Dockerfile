FROM python:3.10-alpine

WORKDIR /audit_alpes-real-estate

COPY . .

COPY config-cloud.py config.py

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 80

CMD [ "flask", "--app", "app/api", "run", "--host=0.0.0.0", "--port", "80"]