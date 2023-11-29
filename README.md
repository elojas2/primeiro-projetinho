# Nome

## Descrição

Projetinho com o intuito de aprender a usar metricas e manipular dashboards com Grafana/Prometheus


## Estrutura do projeto

* app.py: arquivo principal com o codigo da aplicacao Flask
* dockerfile: arquivo para a construcao de imagem da aplicacao
* docker-compose.yml: arquivo de configuracao do ambiente de desenvolvimento
* requirements.txt (?)

### Requisitos necessarios

* Docker
* Docker compose

## Como executar

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




