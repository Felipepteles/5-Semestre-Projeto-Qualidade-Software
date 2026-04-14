# Estratégia Inicial de Testes – LocalEats

## 1. Funcionalidades
- Login
- Busca
- Visualização do cardápio
- Filtragem
- Sistema de avaliações
- Favoritos

---

## 2. Níveis de Teste

### Funcionalidade: Login
- Unitário: validar senha e campos obrigatórios
- Integração: verificar comunicação com banco
- Sistema: usuário faz login completo
- Aceitação: usuário entra no sistema sem erro

### Funcionalidade: Busca
- Unitário: Validar se a função de busca aceita caracteres especiais ou campos vazios
- Integração: Verificar se chegou corretamente no banco
- Sistema: Clica em busca e validar se a lista de resultados aparece mesmo
- Aceitação: Garantir que o cliente consegue achar um restaurante pelo nome de forma rápida

### Funcionalidade: Visualização do cardápio
- Unitário: Validar se a função que calcula o preço total ou formata corretamente
- Integração: Verificar se as imagens estão carregando corretamente
- Sistema: Abrir um perfil de um restaurante e navegar pelas categorias do cardapio
- Aceitação: Valida se a visualização esta legivel e intuitiva (web e mobile)

### Funcionalidade: Filtragem
- Unitário: Testar a ordenação
- Integração: Verificar se combina multiplos filtros
- Sistema: Aplicar um filtro de uma categoria e garantir que nenhum outro apareça na lista
- Aceitação: Confirmar se os filtros reduzem a lista de opções para aquilo que o cliente realmente deseja

### Funcionalidade: Sistema de avaliações
- Unitário: Validar se o campo de comentário respeita o limite máximo de caracteres
- Integração: Testar persistencia após clicar em enviar
- Sistema: Verificar se a media geral do restaurante foi atualizada após completar um fluxo
- Aceitação: Garantir que o processo seja rápido

### Funcionalidade: Favoritos
- Unitário: Validar a função que altera o estado do icone
- Integração: Verificar se a lista de favoritos é sincronizada corretamente
- Sistema: Adicionar um restaurante aos favoritos, fechar o app, abrir novamente e validar se continua na lista
- Aceitação: O cliente deve ser capaz de acessar sua lista de favoritos com apenas um clique

---

## 3. Prioridades e Riscos

Alta prioridade:
- Busca e Filtragem → Se o usuário não encontra o restaurante, a plataforma perde o propósito.

Justificativa:
Falhas nessas áreas impedem o funcionamento básico do modelo de negócio

Baixa prioridade: 
- Favoritos → não impede uso

Justificativa:
Embora importante para o engajamento, o sistema ainda é útil sem recomendações perfeitas

---

## 4. Pirâmide de Testes

- Maior foco: Testar todas as regras de negócio lógicas e validações de formulário
- Médio foco: Validar contratos de API, comunicação com banco de dados e sincronização Web-Mobile
- Menor foco: Testar apenas os fluxos críticos de ponta a ponta

Justificativa:
Testes unitários são baratos e rápidos de executar. Testes de integração resolvem os principais problemas de comunicação.

---

## 5. Testes em Produção

- Uso de: Monitoramento de Performance (APM)
- Aplicar em: Lançamento de correções para a lentidão em horários de pico e novas funcionalidades de sincronização Web/Mobile

Justificativa:
Como o sistema já está em opreção e apresenta letindão intermitente, testes em ambiente controlado podem não replicar o real comportamento. O monitoramento ativo permite identificar exatamente qual consulta ao banco de dados está causando o "desaparecimento" das avaliações.
