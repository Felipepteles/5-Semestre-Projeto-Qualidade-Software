# Aula 9 – Testes Unitários e TDD

## 👥 Integrantes
- Felipe Teles

---

## 📁 Estrutura do Projeto

.  
├── src/  
│   ├── calculadora_entrega.py  
└── tests/  
    ├── test_calculadora_entrega.py 

---

## 🔹 1. Funcionalidades escolhidas

Cálculo de taxa de entrega

---

### 👤 Integrante 1 – Cálculo de taxa de entrega

**Arquivo da implementação:** `/src/calculadora_entrega.py`  
**Arquivo de testes:** `/tests/test_calculadora_entrega.py`

#### Descrição
Soma os valores dos itens do pedido e valida se o total atinge o valor mínimo.

#### Regras de negócio
- Soma dos itens define o total  
- Pedido deve atingir valor mínimo  
- Caso contrário, deve gerar erro  

---

## 🔹 2. Testes Unitários

Cada integrante implementou seus testes unitários no respectivo arquivo dentro da pasta `/tests`.

---

### 🧪 Integrante 1 (Felipe) – Testes (taxa de entrega)

#### Teste 1 – Distância até 3 km (taxa fixa)

- Cenário: Distância menor ou igual ao limite inicial
- Resultado esperado: Retorna a taxa base

##### TDD

- Red: teste falhou por função inexistente ou vazia
- Green: implementação de um condicional básico retornando 5.0
- Refatoração: criação de constantes descritivas para os valores numéricos

##### Refatoração

- Remoção de números mágicos do código
- Melhoria na legibilidade da regra de taxa fixa

##### Execução

- Resultado: Passou

#### Teste 2 – Distância acima de 3 km (taxa proporcional)

- Cenário: Distância excede o limite da taxa fixa
- Resultado esperado: Retorna taxa base somada ao valor por km adicional

##### TDD

- Red: teste falhou pois o código não calculava quilometragem extra
- Green: implementação da conta matemática direta
- Refactor: extração do cálculo para variáveis de fácil leitura

##### Refatoração

- Organização da lógica de cálculo proporcional
- Fluxo de execução mais direto e alinhado com a regra de negócio

##### Execução

- Resultado: Passou

#### Teste 3 – Distância negativa

- Cenário: Entrada com valor de distância inválido
- Resultado esperado: Erro

##### TDD

- Red: teste falhou esperando um erro que não foi gerado pelo código
- Green: exceção ValueError implementada com a mensagem correta
- Refactor: otimização da ordem de validação

##### Refatoração

- Tratamento explícito de erro validado via pytest.raises
- Posicionamento da trava de segurança logo na primeira linha da função

## 🔹 3. Reflexão

### Foi difícil escrever testes antes do código?
Foi práticamente uma mudança de paradigma. Em vez de partir direto para a execução da lógica, é necessário parar e planejar o comportamento, os limites e as restrições da regra de negócio antes, estruturando a base antes de "montar" os componentes do código.

---

### O TDD ajudou no desenvolvimento?
Sim, o processo forçou a quebra do problema em partes menores, permitindo construir a funcionalidade de forma incremental e focada exclusivamente no que era necessário para o teste passar.

---

### Os testes aumentaram a confiança no código?
Muito. A maior vantagem é a rede de segurança contra regressões. Qualquer erro ou impacto colateral gerado por uma alteração no código é detectado rapidamente.

---

### O que melhorariam?
- Análise de Cobertura: Integrar uma ferramenta de relatório para medir matematicamente qual porcentagem do código-fonte está sendo ativada durante a execução da suíte de testes.  
- Cobertura de cenários complexos: Implementar testes parametrizados (usando @pytest.mark.parametrize) para varrer dezenas de valores decimais e entradas inesperadas de uma só vez. 

---

### Como isso ajuda no projeto?
Como desenvolvi e apliquei essas regras de forma individual, os testes atuam como minha principal rede de segurança contra mim mesmo. Em um projeto solo, eu sou responsável por todas as camadas do sistema, portanto ter o núcleo das regras de negócio do LocalEats validado de forma automatizada garante que, a medida que eu avanço na construção do banco de dados ou da interface, minhas atualizações futuras não quebram acidentalmente lógicas que já estavam prontas e funcionando.