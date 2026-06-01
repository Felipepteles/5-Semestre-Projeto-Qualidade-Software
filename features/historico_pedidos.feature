Feature: Histórico de pedidos
Usuário loga na plataforma
Como usuário logado da plataforma LocalEats
Eu quero visualizar meu histórico de transações
Para que eu possa acompanhar os pedidos que já realizei

Scenario: Visualizar pedidos realizados com sucesso
Given que o usuário está na página de pedidos do LocalEats
When a página carregar o histórico de transações
Then o sistema deve exibir a lista de pedidos cadastrados
And o valor total do "Pedido #1" deve estar visível