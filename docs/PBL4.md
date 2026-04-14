# 🧪 Aula 5 – Testes Funcionais vs Estruturais  
## 🎯 1. Funcionalidade escolhida

**Funcionalidade selecionada:**  
Busca de restaurantes (com filtros)
<!-- Ex: Busca de restaurantes, Login, Avaliação, Favoritos -->

**Descrição da funcionalidade:**  
Permite que o cliente encontre restaurantes digitando termos de busca ou aplicando filtros, categoriasm localização e faixa de preço
<!-- Explique brevemente o que a funcionalidade faz -->

**O que o usuário espera:**  
O cliente espera o sistema entregue o resultado preciso e rápido que corresponda exatamente ao que foi aplicado
<!-- Qual é o comportamento esperado do ponto de vista do usuário? -->

---

## 🔍 2. Testes Caixa-Preta (Visão do Usuário)

**Quais testes vocês fariam sem conhecer o código?**

### 🔹 Cenários de teste

- Cenário 1:
Busca simples, digitar "pizza" e verificar se aparecem apenas pizzarias   
- Cenário 2:
Múltiplos filtros, selecionar "japonesa" + "preço baixo" e verificar se a lista é filtrada corretamente    
- Cenário 3:
Busca inexistente, digitar "a1908dm" e verificar se o sistema exibe a mensagem de 0 resultados encontrados    
- Cenário 4:
Localização, buscar por "perto de min" e validar se os primeiros restaurantes são os mais próximos  

---

### 🔹 Possíveis erros identificados

-Resultaods não condizem com o filtro  
-Erros de interface  
-Mensagens de erro confusas  

---

## 🔧 3. Testes Caixa-Branca (Visão do Sistema)

**Como essa funcionalidade poderia estar implementada internamente?**

### 🔹 Lógica hipotética (pseudo-código ou descrição)

```pseudo
function pesquisar(texto, filtroPreco) {
    if (texto == vazio) {
        exibir("Por favor, digite algo")
        break
    }
    if (filtroPreco == "Barato") {
        buscarNoBanco("preco < 30")
    } else {
        buscarNoBanco("todos os preços")
    }
}
```

### 🔹 Situações a serem testadas

- Situação 1  
 Teste do if inicial: O que acontece se o usuário clicar em buscar sem digitar nada? (Garante que a mensagem de erro aparece)

- Situação 2  
  Teste do Filtro: Garantir que ao selecionar "Barato", o código realmente execute a query de valores baixos e não a geral
  
- Situação 3  
  Teste de Fluxo: Garantir que o sistema não tente buscar no banco de dados se a validação do textoBusca falhar
  
### 🔹 Possíveis erros identificados

-Erro de Lógica: O sistema ignorar o filtro de preço e retornar todos os restaurantes (erro no if/else)
-Erro de Null: O sistema travar se o textoBusca vier null em vez de apenas vazio  
-Erro de Mensagem: A mensagem de erro "Por favor, digite algo" não ser disparada por uma falha na condição do primeiro if  

## ⚖️ 4. Comparação entre as abordagens

Qual a principal diferença entre testar sem ver o código e com acesso ao código?

- A principal diferença é o foco, o Caixa-Preta o foco é o comportamento e a conformidade com o requisito. Na Caixa-Branca o foco é a implementação e a robustez lógica  

Que tipo de problema cada abordagem ajuda a encontrar?

Caixa-preta:
- Encontra contradições nos requisitos, erros de usabilidade, funcionalidades  
Caixa-branca:
- Encontra fluxos lógicos mortos (código que nunca é executado), falhas de segurança  

## 💡 5. Reflexão no contexto do LocalEats

Qual abordagem parece mais importante neste momento do projeto?

- Caixa-Preta é prioritária para garantir que o usuário consiga completar o fluxo básico sem frustração  

Apenas uma abordagem seria suficiente? Por quê?

- Usar apenas Caixa-Preta deixaria passar erros de performance escondidos no código, e usar apenas Caixa-Branca poderia resultar em um código "perfeito" que não atende às necessidades reais do usuário  

## 🚀 Conclusão

Enquanto o teste de caixa-preta protege a experiência do cliente, o teste de caixa-branca protege a integridade e a escalabilidade da aplicação, sendo ambos indispensáveis
