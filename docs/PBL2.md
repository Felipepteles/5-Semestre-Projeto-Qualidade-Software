# Diagnóstico da organização da qualidade na startup — PBL 2
**Projeto:** Local Eats


### 1. Papéis atuais identificados
* **Quais papéis provavelmente existem hoje na startup?**
 A equipe provavelmente é pequena, deve conter apenas um desenvolvedor e um gerente.
* **Quem provavelmente está responsável pela qualidade atualmente?**
  Infelizmente sem uma equipe que possa dedicar tempo e esforços pela qualidade, provavelmente o desenvolvedor está responsável, testando o próprio código ou no pior cenario, o cliente testando e descobrindo erros em produção
* **Quais problemas podem ocorrer quando as responsabilidades de qualidade não estão claras?**
  Retrabalho e custos, defeitos geram desperdício de tempo e recursos. A insatisfação dos clientes e parceiros é uma constante ameaça ao negócio.
* **A qualidade deve ser responsabilidade de uma pessoa ou de toda a equipe?**
  A responsabilidade deve ser compartilhada, embora o QA seja responsavel por planejar e validar, o desenvolvedor deve garantir a corretude do código e o PO a clareza dos requisitos.
---
### 2. Definição de papéis da equipe

| Papel | Responsabilidades principais | Relação com a qualidade |
|------|------|------|
|QA |Planejar e executar testes(manuais e automatizados. Gerir bugs e validar critérios |Atua antes da produção, garantindo que o software entregue oque foi prometido sem falhas |
|Dev |Codificar funcionalidades, realizar testes unitários e revisões de codigo |Responsável pela qualidade intrínseca, garantindo um código limpo, seguro e livre de erros |
|PO |Levantar requisitos, detalhar e definir regras de negócio |Garante a adequação funcional, evita que a equipe desenvolva algo que não atende a necessidade real |
|DevOps |Gerenciar ambiente de deploy |Garante a confiabilidade e eficiência, assegura que o sistema suporte picos de acesso sem ficar lento ou cair |

---
### 3. Práticas de QA Sugeridas
* Revisão de Requisitos: Validar as regras de negócio antes de começar a programar, evitando erros de lógica e aumentando a acertividade da entrega.
* Testes de regressão: Sempre que uma falha for corrigida, criar um teste para garantir que o erro nunca mais volte.
* Testes de API: Validar as comunicações entre app e servidor, garantindo que a lógica não permita duplicidade e perca de informações no banco de dados.
* Teste de Carga: Simular varios acessos simultâneos para identificar o limite do sistema.
---
### 4. Anúncios de Contratação

**Vaga 01: QA**  
Empresa: Local Eats  
Local: Híbrido - Pelotas(RS)

***Sobre a vaga:***  
Estamos buscando um QA para reformular a cultura da empresa. Você será o responsável por validar fluxos críticos de pagamento e checkout para evitar pedidos duplicados e inconsistências de dados.  

### Principais Responsabilidades
 * Criar um plano de testes
 * Investigar e reportar bugs
 * Executar testes focados na jornada do usuario

### Requisitos Obrigatorios
 * Conhecimento em tipos de testes (funcional, regressão)
 * Experiência com ferramentas de reporte de bugs

### Requisitos Desejáveis
 * Noções de automação
* Conhecimento em git

---
**Vaga 02: Desenvolvedor Back-end Pleno**  
Empresa: Local Eats  
Local: Híbrido - Pelotas(RS)

***Sobre a vaga:***  
Buscamos uma pessoa com foco em robustez e escalabilidade para lidar com alto volume de pedidos.  

### Principais Responsabilidades
* Desenvolver APIs seguras e performáticas
* Garantir a integridade das transações
* Escrever testes unitários

### Requisitos Obrigatorios
 * Domínio de linguagens backend (Node.js ou PY)
 * Experiência com banco de dados relacionais (PostgreSQL)
 * Foco em escrita de código limpo

### Requisitos Desejáveis
 * Conhecimento em Docker e AWS
 * Experiência prévia em E-Commerce ou delivery
