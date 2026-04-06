# 🧪 Plano de Testes — Sistema de Desconto

**Descrição:**  
Testes realizados para validar o funcionamento de um sistema de desconto simples.

---

## ⚠️ Teste 001 — Validação de números negativos

- **Entrada:** `-1`  
- **Resultado esperado:**  
  O sistema deve exibir uma mensagem de erro sem travar.  
- **Resultado obtido:**  
  ❌ Não exibiu mensagem de erro e continuou a execução mesmo com valor negativo.

---

## ✅ Teste 002 — Validação de entrada com letras

- **Entrada:** `das`  
- **Resultado esperado:**  
  O sistema deve exibir uma mensagem de erro sem travar.  
- **Resultado obtido:**  
  ✔️ Exibiu mensagem de erro corretamente, sem travamento.

---

## ⚠️ Teste 003 — Validação da regra de negócio

- **Entrada:** `70` (70%)
- **Cenário:** As regras de negócio não permitem descontos menores que 0% ou maiores que 50%.
- **Resultado esperado:**  
  O sistema deve exibir uma mensagem de erro clara.  
- **Resultado obtido:**  
   ❌ Não exibiu mensagem de erro e prosseguiu.
  
---

## ⚠️ Teste 004 — Cálculo de desconto

- **Entrada:** `20` (20%)  
- **Cenário:** Aplicar desconto sobre R$100  
- **Resultado esperado:**  
  Valor final deve ser **R$80**.  
- **Resultado obtido:**  
  ❌ O desconto **não foi aplicado**.

---

## 📌 Conclusão

O sistema apresenta falhas em:
- Validação das regras de negócio
- Validação de números negativos
- Aplicação correta do desconto

Por outro lado, a validação de entrada com caracteres inválidos está funcionando corretamente, porém, poderia exibir uma mensagem mais clara dizendo porque o sistema deu erro.
