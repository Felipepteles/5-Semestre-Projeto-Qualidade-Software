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