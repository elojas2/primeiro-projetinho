from flask import Flask, Response
from prometheus_client import Counter, Gauge, generate_latest
import random

app = Flask(__name__)

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

#escolher entre 3 tipos de status_code 200, 300 ou 500
def random_status_code():
    return str(random.choice([200, 300, 500]))

#randomizando um numero entro 10000 e 90000
def random_number():
    return random.randint(10000, 90000)


#metric counter
numero_requests = Counter(
    'numero_requests_total',
    'o numero de requests, contador.',
    ['status_code', 'location']
)

#metric gauge
requests = Gauge(
    'requests',
    'A memoria que esta sendo usada (aleatoriamente).',
    ['server_name', 'location']
)

#primeira pagina que ira gerar algumas metricas
@app.route('/primeira-pagina')
def primeira_pagina():
    numero_requests.labels(random_status_code(), 'primeira-pagina').inc()
    requests.labels('server-a', 'primeira-pagina').set(random_number())
    return "bem vindo a primeira pagina"

#segunda pagina que ira gerar algumas metricas
@app.route('/segunda-pagina')
def segunda_pagina():
    numero_requests.labels(random_status_code(), 'segunda-pagina').inc()
    requests.labels('server-a', 'segunda-pagina').set(random_number())
    return 'bem vindo a segunda pagina'


#visualizacao das metricas
@app.route('/metrics', methods=['GET'])
def get_data():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
