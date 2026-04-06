def calcular_desconto():
    print("=== SISTEMA DE DESCONTOS v1.0 (QA TEST) ===")

try:
    # Requisito 1: Valor da compra deve ser positivo.
    valor_compra = float(input("Digite o valor da compra: "))

    # Requisito 2: Descontos válidos apenas entre 0% e 50%.
    percentual = float(input("Digite o percentual de desconto (ex: 10 para 10%): "))
    valor_final = valor_compra

    (valor_compra * (percentual / 100))

    print(f"\n✅ Processado com sucesso!")
    print(f"Valor Final: R$ {valor_final}")

except ValueError:
    print("Erro no sistema.")
    if __name__ == "__main__":
        calcular_desconto()