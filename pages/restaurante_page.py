class RestaurantePage:
    def __init__(self, page):
        self.page = page
        self.link_restaurante = page.get_by_role("link", name="Restaurante Sabor 2")
        self.botao_adicionar = page.get_by_role("button", name=" Adicionar").first
        self.botao_finalizar = page.get_by_role("button", name="Finalizar Pedido")
        self.mensagem_sucesso = page.get_by_text("Pedido Realizado!")

    def fazer_pedido(self):
        self.link_restaurante.click()
        self.botao_adicionar.click()
        self.botao_finalizar.click()

    def obter_mensagem_sucesso(self):
        return self.mensagem_sucesso