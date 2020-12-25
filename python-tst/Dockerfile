FROM python:3

ADD src /src

WORKDIR /src

RUN pip install -r requirements.txt

EXPOSE 5000
ENV  ELASTIC_APM_SERVICE_NAME=tst
ENV  ELASTIC_APM_SECRET_TOKEN=changeme
ENV  ELASTIC_APM_SERVER_URL=http://localhost:8200
ENV  FLASK_APP=app

CMD flask run
