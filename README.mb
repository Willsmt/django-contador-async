# django-contador-async

> Projeto de estudo sobre concorrência em Django — views síncronas vs. assíncronas, event loop e ASGI.

Projeto desenvolvido com **Django 6.0** como parte do curso Desenvolvedor Full Stack Python (EBAC), módulo *Concorrência em Django*.

## Stack

- Python 3.12+
- Django 6.0
- Uvicorn (servidor ASGI)
- HTTPX (cliente HTTP sync/async)
- SQLite (desenvolvimento)
- python-decouple (variáveis de ambiente)

## Estrutura

```
django-contador-async/
├── core/          # configuração do projeto (settings, urls, wsgi, asgi)
├── contador/       # app com as views de demonstração
├── manage.py
├── .env            # variáveis sensíveis (não versionado)
└── .gitignore
```

## Endpoints

| Rota | Tipo | O que demonstra |
|---|---|---|
| `/contador/` | Assíncrona | Cliente espera o resultado, mas o event loop fica livre pra atender outras requisições nesse meio tempo — concorrência **entre requisições diferentes**. |
| `/contador/http-async/` | Assíncrona (`create_task`) | Resposta imediata (`HttpResponse`) enquanto um contador de 1 a 5 e uma chamada HTTP continuam rodando em background, no mesmo event loop — fire-and-forget **dentro da mesma requisição**. |
| `/contador/http-sync/` | Síncrona | Mesmo comportamento do `http-async`, só que bloqueante — trava a resposta até o contador e a chamada HTTP terminarem. Serve de contraste. |

Pra ver a diferença de verdade entre os dois modelos de concorrência, rode sob Uvicorn (não `runserver`) e dispare duas requisições simultâneas em `/contador/?segundos=5`.

## Rodando localmente

```bash
# 1. Clonar e entrar no diretório
git clone git@github.com:Willsmt/django-contador-async.git
cd django-contador-async

# 2. Criar e ativar o ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Criar o arquivo .env na raiz
echo "SECRET_KEY=sua-chave-secreta-aqui" > .env
echo "DEBUG=True" >> .env
echo "ALLOWED_HOSTS=localhost,127.0.0.1" >> .env

# 5. Aplicar migrações
python manage.py migrate

# 6. Subir o servidor via ASGI (Uvicorn)
uvicorn core.asgi:application --reload
```

Acesse `http://127.0.0.1:8000/contador/` para ver a aplicação.

## Segurança

A `SECRET_KEY` e demais dados sensíveis são carregados via variáveis de ambiente (`.env`), nunca versionados no repositório.

---

Desenvolvido por [Willians](https://github.com/Willsmt) — *dev com visão de segurança*.
