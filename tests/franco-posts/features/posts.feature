Feature: Crud de Posts - Franco
    Como usuário da API
    Quero realizar operações de CRUD no recurso de Posts

    Background:
        Given que a url base da API é "http://localhost:3000"
        And que o endpoint de posts é "/post" 

    Scenario: Listar todos os Posts Cadastrados
        Given que tenho posts cadastrados no sistema
        When envio uma requisição GET para /post
        Then o sistema deve retornar status 200
        And deve retornar uma lista de posts
        And cada post deve conter os campos "post_id", "descricao", "imagem", "local_id", "usuario_id", "created_at", "updated_at"

    Scenario: Listar um post ao buscar por ID
        Given que tenho posts cadastrados no sistema
        When pesquiso pelo post com ID 1
        Then o sistema deve retornar status 200
        And o campo "post_id" deve ser igual a 1

    Scenario: Criar um novo post com sucesso
        When envio um novo post com descricao "Novo Post", usuario 2 e local 3
        Then o sistema deve retornar status 201
        And o campo "descricao" deve ser igual a "Novo Post"
        And o campo "usuario_id" deve ser igual a 2

    Scenario: Atualizar um post existente com sucesso
        Given que tenho posts cadastrados no sistema
        When atualizo o post criado anteriormente com a nova descricao "100% atualizado"
        Then o sistema deve retornar status 200
        And o campo "descricao" deve ser igual a "100% atualizado"