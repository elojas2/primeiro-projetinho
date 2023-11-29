# Primeiro projetinho mexendo com Grafana, prometheus e metricas

## Descrição

Projetinho com o intuito de aprender a usar metricas e manipular dashboards com Grafana/Prometheus.
Nesse projeto, foram usados funcoes para criar valores aleatorios para o uso das metricas. Foram criadas as duas metricas, um NUMERO_REQUESTS usando o Counter e outra chamada REQUESTS utilizando o Gauge. Tanto o Gauge quanto o Counter foram importadas da biblioteca prometheus_client.


## Estrutura do projeto

* app.py: arquivo principal com o codigo da aplicacao Flask
* dockerfile: arquivo para a construcao de imagem da aplicacao
* docker-compose.yml: arquivo de configuracao do ambiente de desenvolvimento

### Requisitos necessarios

* Docker
* Docker compose

## Passo de como executar

1. clone o repositorio
    ``` git clone https://github.com/elojas2/primeiro-projetinho.git ```

2. inicie e construa a imagem com o docker-compose
    ``` docker-compose up --build ```


Pronto, assim será inicializado o Grafana, Prometheus e o app em Flask

* o aplicativo Flask estará disponível em http://localhost:5000
* o Prometheus estará disponível em http://localhost:9090
* o Grafana estará disponível em http://localhost:3000


#### Atencao sobre o grafana

Em caso do Grafana pedir usuario e senha: 
* o usuario: admin
* a senha: admin

## Arquivo principal

#### app.py

como dito anteriormente, esse arquivo contem a aplicacao em Flask e nele contem as rotas para diferentes endpoints, são eles:

* http://localhost:5000/metrics
* http://localhost:5000/primeira-pagina
* http://localhost:5000/segunda-pagina

#### para que sejam geradas as metricas, va no navegador e digite ou cole as seguintes URLs:

1. http://localhost:5000/primeira-pagina
2. http://localhost:5000/segunda-pagina

para verificar as metricas, escreve ou cole no navegador a seguinte URL:

* http://localhost:5000/metrics

#### Para encerrar

clique com as teclas ``` CTRL + C ``` no terminal
