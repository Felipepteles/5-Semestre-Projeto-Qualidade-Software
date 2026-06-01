# Aula 12 – BDD e Automação Orientada a Comportamento
# Exemplo de Entrega PBL – LocalEats

## 👥 Integrantes

- Felipe Teles

---

# 🔹 1. Fluxo escolhido

## Integrante: Felipe Teles

### Fluxo
Histórico de pedidos

### Objetivo
Validar se os pedidos realizados pelo usuário são exibidos corretamente com seus respectivos valores.

---

# 🔹 2. Cenários BDD

## Arquivo

```text
features/historico_pedidos.feature
```

## Conteúdo

```gherkin
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
```

---

# 🔹 3. Automação com pytest-bdd

## Estrutura do projeto

```text
projeto/
│
├── features/
│   └── historico_pedidos.feature
│
├── tests/
│   └── test_historico_pedidos.py
│
├── evidencias/
│
└── README.md
```

---

## Arquivo

```text
tests/test_historico_pedidos.py
```

## Código

```python
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import Page, expect

scenarios('../features/historico_pedidos.feature')

@given('que o usuário está na página de pedidos do LocalEats')
def acessar_pagina_pedidos(page: Page):
    page.goto("https://local-eats-unisenac.vercel.app/static/login.html")
    page.get_by_role("textbox", name="teste@teste.com").fill("fpteles7@gmail.com")
    page.get_by_role("textbox", name="Sua senha secreta").fill("senha123")
    page.locator("#loginForm").get_by_role("button", name="Entrar").click()
    page.wait_for_timeout(1000) 
    page.goto("https://local-eats-unisenac.vercel.app/static/orders.html")

@when('a página carregar o histórico de transações')
def aguardar_carregamento_historico(page: Page):
    expect(page.locator('text=Histórico de Transações')).to_be_visible()

@then('o sistema deve exibir a lista de pedidos cadastrados')
def validar_lista_pedidos(page: Page):
    expect(page.locator('.order-title').first).to_be_visible()

@then('o valor total do "Pedido #1" deve estar visível')
def validar_valor_pedido(page: Page):
    expect(page.locator('text=R$ 59.17').first).to_be_visible()
```

---

# 🔹 4. Execução dos testes

## Comando executado

```bash
pytest -v
```

---

## Resultado

```text
=================== test session starts ===================

6 passed in 12.01s

==========================================================
```

---

# 🔹 5. Evidências

## Print da execução

```text
evidencias/
  execucao-testes.png
```

![alt text](/evidencias/execucao-testes.png)

## Print da aplicação

```text
evidencias/
  historico-pedidos.png
```

![alt text](/evidencias/historico-pedidos.png)
---

# 🔹 6. Análise crítica

## O cenário ficou legível?

Sim. O formato (Gherkin) explica exatamente o que vai acontecer no teste, sem misturar com código de programação.

---

## O BDD ajudou a entender o comportamento?

Com certeza. Fica fácil para qualquer pessoa da equipe (como o dono do restaurante) ler o arquivo e entender como o sistema deve funcionar.

---

## O teste ficou robusto?

Parcialmente. Como usamos textos exatos da tela (ex: "R$ 59.17"), o teste pode falhar facilmente se houver uma mudança de layout.

---

## Quais dificuldades surgiram?

- Lidar com o "Strict Mode" do Playwright (o teste quebrava quando achava vários pedidos na mesma tela).
- Problemas de formatação do sistema (o teste esperava ponto ao invés de vírgula no preço).
- Configurar o login para rodar antes de acessar a página protegida de pedidos.

---

## O teste ficou dependente da interface?

Bastante. Se o desenvolvedor mudar o nome da classe HTML ou o texto do botão, o código de automação no Python precisará ser corrigido.

---

# 🔹 7. Reflexão final

## BDD melhora comunicação entre equipe?

Sim, pois cria uma linguagem única. Desenvolvedores, QA e a área de negócios conseguem ler o mesmo documento e concordar com o que precisa ser feito.

---

## Todo teste deve usar BDD?

Não. O BDD dá bastante trabalho para configurar. Ele deve ser usado apenas nos caminhos principais do sistema (como finalizar compra ou login).

---

## Quando vale a pena usar BDD?

Quando a regra do sistema é importante e precisa virar uma "documentação" clara de como o software deve se comportar na visão do usuário.

---

## Como isso ajuda no projeto do grupo?

Ajuda a transformar requisitos em testes automatizados compreensíveis e organizados.

---

# 📦 Repositório GitHub

```text
https://github.com/Felipepteles/5-Semestre-Projeto-Qualidade-Software
```

---

# ✅ Conclusão

A atividade permitiu compreender:

- escrita de cenários BDD
- escrever as regras do sistema de forma simples usando Gherkin.
- conectar essas regras ao código em Python usando pytest-bdd.
- resolver problemas reais de automação no Playwright (como o uso do .first).