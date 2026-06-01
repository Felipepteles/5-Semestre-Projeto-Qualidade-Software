import pytest
from pages.restaurante_page import RestaurantePage
from playwright.sync_api import Page, expect

def test_adicionar_item_carrinho(page: Page):
    page.goto("https://local-eats-unisenac.vercel.app/static/login.html")
    page.get_by_role("textbox", name="teste@teste.com").click()
    page.get_by_role("textbox", name="teste@teste.com").fill("fpteles7@gmail.com")
    page.get_by_role("textbox", name="Sua senha secreta").click()
    page.get_by_role("textbox", name="Sua senha secreta").fill("senha123")
    page.locator("#loginForm").get_by_role("button", name="Entrar").click()
    page.get_by_role("link", name="Restaurante Sabor 2").click()
    page.get_by_role("button", name=" Adicionar").first.click()
    page.get_by_role("button", name="Finalizar Pedido").click()

    mensagem_sucesso = page.get_by_text("Pedido Realizado!") 
    expect(mensagem_sucesso).to_be_visible()
