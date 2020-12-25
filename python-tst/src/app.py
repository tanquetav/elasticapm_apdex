from elasticapm.contrib.flask import ElasticAPM
from flask import Flask
from random import random
from time import sleep

app = Flask(__name__)

@app.route('/')
def bar():
    sleep (random()*5)
    return "ok"

apm = ElasticAPM(app)
