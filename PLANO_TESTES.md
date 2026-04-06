# 🧪 Plano de Testes — Sistema de Desconto

**Descrição:**  
Testes realizados para validar o funcionamento de um sistema de desconto simples.

---

## ✅ Teste 001 — Validação de números negativos

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

## ⚠️ Teste 003 — Cálculo de desconto

- **Entrada:** `20` (20%)  
- **Cenário:** Aplicar desconto sobre R$100  
- **Resultado esperado:**  
  Valor final deve ser **R$80**.  
- **Resultado obtido:**  
  ❌ O desconto **não foi aplicado**.

---

## 📌 Conclusão

O sistema apresenta falhas em:
- Validação de números negativos
- Aplicação correta do desconto

Por outro lado, a validação de entrada com caracteres inválidos está funcionando corretamente.
