# Projeto-FastAPI-SQLAlchemy


# Tech Store API

Esta é uma API para uma loja de tecnologia, desenvolvida usando FastAPI, SQLAlchemy e fastapi-pagination.

## Funcionalidades

- Adicionar produtos com nome, descrição, e preço.
- Filtrar produtos por nome.
- Customizar a resposta dos endpoints para incluir nome, descrição e preço.
- Manipular exceções de integridade dos dados.
- Adicionar paginação aos resultados utilizando fastapi-pagination.

## Requisitos

- Python 3.7+
- FastAPI
- SQLAlchemy
- fastapi-pagination
- Uvicorn

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/tech-store-api.git
    cd tech-store-api
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Rode o servidor:
    ```sh
    uvicorn app.main:app --reload
    ```

5. A API estará disponível em `http://127.0.0.1:8000`.

## Endpoints

### Adicionar Produto

- **URL:** `/produtos/`
- **Método:** `POST`
- **Corpo da Requisição:**
    ```json
    {
        "nome": "Nome do Produto",
        "descricao": "Descrição do Produto",
        "preco": 100.0
    }
    ```
- **Resposta:**
    ```json
    {
        "id": 1,
        "nome": "Nome do Produto",
        "descricao": "Descrição do Produto",
        "preco": 100.0
    }
    ```

### Listar Produtos

- **URL:** `/produtos/`
- **Método:** `GET`
- **Parâmetros de Query:**
    - `nome` (opcional): Filtrar por nome do produto
- **Resposta:**
    ```json
    {
        "items": [
            {
                "id": 1,
                "nome": "Nome do Produto",
                "descricao": "Descrição do Produto",
                "preco": 100.0
            }
        ],
        "total": 1,
        "limit": 10,
        "offset": 0
    }
    ```

## Manipulação de Erros

- Ao tentar adicionar um produto com um nome já existente, a API retorna:
    - **Código de Status:** `303`
    - **Resposta:**
        ```json
        {
            "detail": "Já existe um produto cadastrado com o nome: Nome do Produto"
        }
        ```

## Paginação

- Utilize os parâmetros `limit` e `offset` para paginar os resultados no endpoint `/produtos/`.

## Estrutura do Código

### app/__init__.py

```python
# Este arquivo pode ser vazio ou conter metadados da aplicação
