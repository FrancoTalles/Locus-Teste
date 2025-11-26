Feature: Crud de Comentarios - Joao Menezes
    Como usuário da API
    Quero realizar operações de criação de comentários no recurso de Comentarios

    Background:
        Given que a url base da API é "http://72.61.43.201"
        And que o endpoint de comentarios é "/comentarios" 
    
    Scenario: Criar um novo comentario
        When envio um novo comentario "Novo Comentario" do usuario 4 no post 2
        Then o sistema deve retornar status 201
        And o campo "comentario" deve ser igual a "Novo Comentario"
        And o campo "usuario_id" deve ser igual a 4

    Scenario: Listar todos os Comentários Cadastrados
        Given que tenho comentarios cadastrados no sistema
        When envio uma requisição GET para /comentarios
        Then o sistema deve retornar status 200
        And deve retornar uma lista de comentários
        And cada comentário deve conter os campos "comentario, usuario_id, updated_at, post_id, comentario_id, created_at"

    Scenario: Listar um comentário ao buscar por ID
        Given que tenho comentarios cadastrados no sistema
        When pesquiso pelo comentário com ID 3
        Then o sistema deve retornar status 200
        And o campo "post_id" deve ser igual a 2
    
    Scenario: Atualizar um comentario existente
        Given que tenho comentarios cadastrados no sistema
        When atualizo o comentário criado anteriormente com o novo texto "comentario atualizado"
        Then o sistema deve retornar status 200
        And o campo "comentario" deve ser igual a "comentario atualizado"
    
    
  Scenario: Deletar um comentário existente
        Given que tenho comentarios cadastrados no sistema
        When removo o comentário criado anteriormente
        Then o sistema deve retornar status 200
        And ao pesquisar pelo ID removido o sistema deve retornar 404