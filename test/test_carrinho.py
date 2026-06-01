import pytest
from playwright.sync_api import Page, expect
from pages.login import LoginPage
from pages.restaurante_page import RestaurantePage

def test_adicionar_item_carrinho_refatorado(page: Page):
    login_page = LoginPage(page)
    restaurante_page = RestaurantePage(page)
    
    login_page.acessar()
    login_page.realizar_login("fpteles7@gmail.com", "senha123")
    
    restaurante_page.fazer_pedido()

    expect(restaurante_page.obter_mensagem_sucesso()).to_be_visible()