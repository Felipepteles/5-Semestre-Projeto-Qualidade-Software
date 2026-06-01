# 🧩 Atividade PBL – Aula 10  
## Testes Funcionais Automatizados – LocalEats

---

## 👥 Integrante(s)
- Felipe Teles 

---

## 🔹 1. Fluxo funcional escolhido

### 📌 Fluxo:
Adição de item ao carrinho.

🔎 **Descrição**  
Adiciona produtos ao carrinho.

🎯 **Importância**  
Parte central do fluxo de compra. Se o carrinho falhar, a plataforma não gera receita, afetando diretamente os restaurantes e o negócio do LocalEats.

---

## 🔹 2. Teste com Codegen

### 💻 Comando utilizado

```bash
playwright codegen https://local-eats-unisenac.vercel.app/
```

### 🔗 Link para o código gerado

👉 https://github.com/seu-repositorio/tests/codegen_login.py

### 🧠 Observações

- O Codegen ajudou a iniciar rapidamente o teste  
- O código gerado é verboso  
- Foi necessário refatorar  

---

## 🔹 3. Teste automatizado com Pytest

### 🔗 Link para o teste

👉 https://github.com/Felipepteles/5-Semestre-Projeto-Qualidade-Software/tests/test_carrinho_bruto.py

### 📌 O que o teste faz?

- Acessa o sistema e realiza o login do usuário 
- Navega até o primeiro restaurante da lista e adiciona o primeiro item ao carrinho 
- Validação Fundamental: Utiliza o expect 

---

## 🔹 4. Refatoração com Page Object Model (POM)

### 🔗 Link para Page Object

👉 https://github.com/Felipepteles/5-Semestre-Projeto-Qualidade-Software/pages/restaurante_page.py

### 🔗 Link para teste refatorado

👉 https://github.com/Felipepteles/5-Semestre-Projeto-Qualidade-Software/tests/test_carrinho.py

### 🧠 Melhorias realizadas

- Separação entre teste e lógica de UI  
- Código mais organizado  
- Maior reutilização  

---

## 🔹 5. Execução dos testes

### ▶️ Comando

```bash
pytest
```

### 📊 Resultado

- Total de testes: 5  
- Testes passaram: 0  
- Testes falharam: 0  

### 📸 Evidência

![alt text](/evidencias/image.png)

---

## 🔹 6. Análise crítica

- A gravação inicial pelo Codegen expôs o risco de criar testes altamente acoplados a dados estáticos.
- A adoção do padrão POM foi fundamental. Ela provou que separar a estrutura de componentes visuais.  
- Teste precisa de melhorias para ser mais robusto  

---

## 🔹 7. Reflexão

- Testes automatizados não substituem testes manuais  
- Devem focar em fluxos críticos  
- Tentar automatizar toda a interface do sistema geraria um alto custo de manutenção.

---

## 💡 Conclusão

A automação de testes funcionais vai muito além de simular cliques. Ela exige engenharia de software aplicada. Ao adotar padrões de arquitetura e boas práticas de codificação, transformamos o que poderia ser um passivo de manutenção em um ativo estratégico, garantindo estabilidade, entregas mais rápidas e confiança total na qualidade do produto final.