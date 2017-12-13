# API REST Framework

# Especificações e Requisitos do Projeto
Desenvolvimento de um projeto para agendamento de consultas usando REST para integração.

#### APP Agendamento:
- Data da Consulta
- Horário de Inicio
- Horário final
- Paciente
- Procedimento

#### API REST deve efetuar as seguintes interações
- Listagem de agendamentos
- Detalhes de um agendamento
- Cadastro de um novo agendamento
- Atualização de um agendamento
- Exclusão de um agendamento


## Tecnologias
Neste projeto foi usado as seguintes tecnologias
Django framework versão 1.11.8,
Django REST Framework versão 3.7.3,
Linguagem de programação Python 2.7+
Banco de dados Sqlite3.

## Sobre o Projeto
[Django](https://www.djangoproject.com/) é um framework muito estável onde existe uma comunidade sempre trabalhando para melhorias
deixando sempre atualizado, corrigindo bugs e melhorando a segurança, a versão usada neste projeto foi 1.11.8 no momento é a mais atualizada para a versão long-term support (LTS)

[Django REST] (http://www.django-rest-framework.org/) na versão 3.7.3, foi usado para criar o API REST responsável pela integração, esse framework é bem robusto e atende as necessidades de um grande ou pequeno projeto umas da vantagens dele é a grande familiaridade com o Django tornando assim uma programação mais simples para manutenção e melhorias do projeto

Linguagem de programação Python 2.7+ foi usado por estar mais familiarizado
tendo pouco tempo para o projeto.

Banco de dados [SQLite] (https://www.sqlite.org/) em sua versão 3 foi usado neste projeto por ser default do Django e também  por ser um projeto pequeno ele atende todas as necessidades de forma aceitável.

Para o desenvolvimento foi usado a linguagem de programação Python na verão 2.7+

## Preparando o Ambiente isolado instalando o projeto e pacotes

**1. Crie o ambiente virtual**:
[virtualenv](http://virtualenv.readthedocs.org/) venv

**2. Download do projeto, via git clone**:
`$ git clone https://github.com/GilsonLeite/Agenda_api_rest.git`

O ambiente virtual (venv) e o projeto (Agenda_api_rest) vai ficar na mesma pasta
para confirmar digite ls enter que vai listar

**3. Ativando o Ambiente**:
`$ cd venv` enter
`$ cd source bin/activate` enter
o ambiente fica ativo quando esta entre parênteses (venv)

**4. Acessar projeto e instalar pacotes**:
Com o ambiente ativado faça o seguinte
`$(venv) cd ../Agenda_api_rest/app` enter

**5. Instalando os pacotes:**
Este arquivo esta dentro do diretório app
`pip install -r requirements.txt`


**6. Executando o projeto:**
Execute o seguinte comendo
`python manage.py runserver`

**7. Acessando APP Agenda:**
http://127.0.0.1:8000/agenda/



### Manipuladores e Roteamento
**Método**|**URL**|**Ação**
:--:|:--:|:--:
GET|`http://127.0.0.1:8000/api/agenda/`|lista os agendamentos
GET|`http://127.0.0.1:8000/api/agenda/``<slug>`|Detalhe do agendamento
POST|`http://127.0.0.1:8000/api/agenda/create/`|cria um novo agendamento
PUT|`http://127.0.0.1:8000/api/agenda/<slug>/update/`|atualiza um agendamento
DELETE|`http://127.0.0.1:8000/api/agenda/<slug>/delete/`|deleta um agendamento

**Estrutura**
Para facilitar a interação foi colocado um Hyperlink 

```json
[
    {
      "id": 18,
      "data": "14-12-2017",
      "inicio": "09:35:54",
      "fim": "10:35:55",
      "paciente": "Moises",
      "procedimento": "Nutricionista",
      "delete": "http://127.0.0.1:8000/api/agenda/moises/delete/",
      "update": "http://127.0.0.1:8000/api/agenda/moises/update/"
  }
]
```

### Para visualizar somente o JSON ##
inserir no final format=json
http://127.0.0.1:8000/api/agenda/<slug>/?format=json
